"""Public-only MCP acceptance. No credentials or third-party packages needed."""
import json
import ssl
from pathlib import Path
from urllib.error import HTTPError
from http.client import HTTPSConnection
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
HEADERS = {'User-Agent': 'Postclick-Public-Check/1.0', 'X-Postclick-Test': '1', 'Content-Type': 'application/json'}

def read(url, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    parts = urlsplit(url)
    if parts.scheme != 'https' or parts.hostname not in {'mcp.ppc.io', 'ppc.io'} or parts.port or parts.username:
        raise ValueError('Only public Postclick HTTPS endpoints are allowed')
    # Python 3.9+ with explicit certificate and hostname verification; no redirects.
    # nosemgrep: python.lang.security.audit.httpsconnection-detected.httpsconnection-detected
    connection = HTTPSConnection(parts.hostname, timeout=30, context=ssl.create_default_context())
    try:
        connection.request('GET' if data is None else 'POST', parts.path or '/', body=data, headers=HEADERS)
        response = connection.getresponse()
        if not 200 <= response.status < 300:
            raise HTTPError(url, response.status, 'Public check failed', response.headers, None)
        return response.read()
    finally:
        connection.close()

def rpc(method, params=None):
    return json.loads(read('https://mcp.ppc.io', {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params or {}}))

def check():
    manifest = json.loads(read('https://mcp.ppc.io/server.json'))
    assert manifest == json.loads((ROOT / 'server.json').read_text()), 'Refresh server.json from the source'
    assert read('https://mcp.ppc.io/llms.txt').decode() == (ROOT / 'AGENT-GUIDE.md').read_text(), 'Refresh the agent guide'
    tools = rpc('tools/list')['result']['tools']
    assert {'list_cro_skills', 'run_cro_skill', 'check_balance'} <= {tool['name'] for tool in tools}
    result = rpc('tools/call', {'name': 'list_cro_skills', 'arguments': {}})['result']
    assert not result.get('isError'), 'Public skill read failed'
    skills = result['structuredContent']['skills']
    assert len(skills) == len(list((ROOT / 'skills').glob('*/SKILL.md'))) > 0
    for skill in skills:
        name = skill['name']
        assert name.startswith('postclick-') and '/' not in name and '..' not in name
        local = ROOT / 'skills' / name / 'SKILL.md'
        remote = read('https://ppc.io/skills/' + name + '/SKILL.md').decode()
        assert local.read_text() == remote, 'Refresh skill ' + name
    try:
        rpc('tools/call', {'name': 'get_audit', 'arguments': {'audit_id': '11111111-1111-4111-8111-111111111111'}})
        raise AssertionError('Private audit request was not refused')
    except HTTPError as error:
        assert error.code == 401 and error.headers.get('www-authenticate'), 'Expected OAuth challenge'
    print(json.dumps({'public_skills': len(skills), 'tools': len(tools), 'private_access': '401', 'version': manifest['version'], 'paid_work_started': False}))

if __name__ == '__main__':
    check()
