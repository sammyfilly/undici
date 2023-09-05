import urllib


def web_socket_do_extra_handshake(request):
    url_parts = urllib.parse.urlsplit(request.uri)
    max_age = "; Max-Age=0" if "clear" in url_parts.query else ""
    value = "1"
    if "value" in url_parts.query:
        value = urllib.parse.parse_qs(url_parts.query)["value"][0]
    cookies = [
        f"samesite-unspecified={value}; Path=/{max_age}",
        f"samesite-lax={value}; Path=/; SameSite=Lax{max_age}",
        f"samesite-strict={value}; Path=/; SameSite=Strict{max_age}",
        f"samesite-none={value}; Path=/; SameSite=None; Secure{max_age}",
    ]
    for cookie in cookies:
        request.extra_headers.append(("Set-Cookie", cookie))


def web_socket_transfer_data(request):
    # Expect close() from user agent.
    request.ws_stream.receive_message()
