""" About cookies."""

###### Signing Outgoing Response Cookies

class SignedCookiesMiddleware(object):
    def process_response(self, request, response):
        for (key, morsel) in response.cookies.items():
            response.set_signed_cookie(key, morsel.value,
                    max_age=morsel['max-age'],
                    expires=morsel['expires'],
                    path=morsel['path'],
                    domain=morsel['domain'],
                    secure=morsel['secure']
            )
            return response

###
class SignedCookiesMiddleware(object):
    def process_response(self, request, response):
        for (key, morsel) in response.cookies.items():
            if morsel['max-age'] == 0:
                # Deleted cookies don't need to be signed
                continue
            response.set_signed_cookie(key, morsel.value,
                    max_age=morsel['max-age'],
                    expires=morsel['expires'],
                    path=morsel['path'],
                    domain=morsel['domain'],
                    secure=morese['secure']
            )
            return response

###### Validating Incoming Request Cookies

class SignedCookiesMiddleware(object):
    def process_request(self, request):
        for key in request.COOKIES:
            request.COOKIES[key] = request.get_signed_cookie(key)

### catching the exception and removing those cookies
from django.core.signing import BadSignature, SignatureExpired

class SignedCookiesMiddleware(object):
    def process_request(self, request):
        for (key,signed_value) in request.COOKIES.items():
            try:
                request.COOKIES[key] = request.get_signed_cookie(key)
            except (BadSignature, SignatureExpired):
                # Invalid cookies should behave as if they were never sent
                del request.COOKIES[key]

######
