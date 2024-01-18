import requests

'''
    url: str | bytes,
    params: _Params | None = None,
    *,
    data: _Data | None = ...,
    headers: _HeadersMapping | None = ...,
    cookies: RequestsCookieJar | _TextMapping | None = ...,
    files: _Files | None = ...,
    auth: _Auth | None = ...,
    timeout: _Timeout | None = ...,
    allow_redirects: bool = ...,
    proxies: _TextMapping | None = ...,
    hooks: _HooksInput | None = ...,
    stream: bool | None = ...,
    verify: _Verify | None = ...,
    cert: _Cert | None = ...,
    json: Any | None = ...
) -> Response
'''

req = requests.get('https://www.python.org')
print(req.status_code)
print(req.content)
print(req.text)
print(req.headers)
print(req.url)
print(req.cookies)
print(req.history)
print(req.encoding)
print(req.elapsed)
print(req.request)
print(req.json)
print(req.iter_lines)
print(req.iter_content)

payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)


with requests.Session() as s:
    s.get('https://httpbin.org/get')
    print(s.headers)