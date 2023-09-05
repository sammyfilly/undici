def main(request, response):
    return request.url if b"full" in request.GET else request.request_path
