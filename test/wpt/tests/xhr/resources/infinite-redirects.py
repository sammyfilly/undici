from wptserve.utils import isomorphic_encode

def main(request, response):
    location = f"{request.url_parts.scheme}://{request.url_parts.netloc}{request.url_parts.path}"
    page = u"alternate"
    mix = 0
    if request.GET.first(b"page", None) == b"alternate":
        page = u"default"

    type = 301 if request.GET.first(b"type", None) == b"301" else 302
    if request.GET.first(b"mix", None) == b"1":
        mix = 1
        type = 302 if type == 301 else 301

    new_location = f"{location}?page={page}&type={type}&mix={mix}"
    headers = [(b"Cache-Control", b"no-cache"),
               (b"Pragma", b"no-cache"),
               (b"Location", isomorphic_encode(new_location))]
    return 301, headers, f"Hello guest. You have been redirected to {new_location}"
