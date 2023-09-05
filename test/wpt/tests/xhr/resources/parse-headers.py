def main(request, response):
    if b"my-custom-header" in request.GET:
        val = request.GET.first(b"my-custom-header")
        response.headers.set(b"My-Custom-Header", val)
    return u""
