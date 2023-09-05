import imp
import os

from wptserve.utils import isomorphic_decode

here = os.path.dirname(isomorphic_decode(__file__))

def main(request, response):
    response.headers.set(b'Access-Control-Allow-Origin', request.headers.get(b"origin"))
    response.headers.set(b'Access-Control-Allow-Credentials', b'true')
    response.headers.set(b'Access-Control-Allow-Methods', b'GET')
    response.headers.set(b'Access-Control-Allow-Headers', b'x-user, x-pass')
    response.headers.set(b'Access-Control-Expose-Headers', b'x-challenge, xhr-user, ses-user')
    auth = imp.load_source(u"", os.path.join(here,
                                             os.pardir,
                                             u"authentication.py"))
    return b"" if request.method == u"OPTIONS" else auth.main(request, response)
