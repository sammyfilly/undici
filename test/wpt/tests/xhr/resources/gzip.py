import gzip as gzip_module

from io import BytesIO

def main(request, response):
    output = request.GET[b"content"] if b"content" in request.GET else request.body
    out = BytesIO()
    with gzip_module.GzipFile(fileobj=out, mode="w") as f:
        f.write(output)
    output = out.getvalue()

    headers = [(b"Content-type", b"text/plain"),
               (b"Content-Encoding", b"gzip"),
               (b"X-Request-Method", request.method),
               (b"X-Request-Query", request.url_parts.query if request.url_parts.query else b"NO"),
               (b"X-Request-Content-Length", request.headers.get(b"Content-Length", b"NO")),
               (b"X-Request-Content-Type", request.headers.get(b"Content-Type", b"NO")),
               (b"Content-Length", len(output))]

    return headers, output
