import datetime

def main(request, response):
    response.headers.set(b"Content-type", b"text/plain")

    expiration = -datetime.timedelta(days=1) if request.GET.get(b"clear") else None
    response.set_cookie(b"WK-test", b"1", expires=expiration)
    response.set_cookie(b"WK-test-secure", b"1", secure=True,
                        expires=expiration)
    content = b""
    for cookie in request.cookies:
        content = content + b" " + cookie + b"=" + request.cookies.get(cookie).value
    response.content = content
