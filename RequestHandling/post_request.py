import requests

'''
    url: str | bytes,
    data: _Data | None = None,
    json: Any | None = None,
    *,
    params: _Params | None = ...,
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
    cert: _Cert | None = ...
) -> Response
'''
req = requests.post()
