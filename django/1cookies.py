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

###### Signing Cookies As a Decorator with salt and max_age

from django.core.signing import BadSignature, SignatureExpired

class SignedCookiesMiddleware(object):
    def __init__(self, salt='', max_age=None):
        self.salt = salt
        self.max_age = max_age

    def process_request(self, request):
        for (key, signed_value) in request.COOKIES.items():
            try:
                request.COOKIES[key] = request.get_signed_cookie(key,
                        salt=self.salt,
                        max_age=self.max_age)
            except (BadSignature, SignatureExpited):
                # Invalid cookies should behave as if they were never sent
                del request.COOKIES[key]

    def process_response(self, request, response):
        for (key, morsel) in response.cookies.items():
            if morsel['max-age'] == 0:
                # Deleted cookies don't need to be signed
                continue
            response.set_signed_cookie(key, morsel.value,
                    salt=self.salt
                    max_age=self.max_age or morsel['max-age'],
                    expires=morsel['expires'],
                    path=morsel['path'],
                    domain=morsel['domain'],
                    secure=morsel['secure']
            )
        return response

### and with decorator
from django.utils.decorators import decorator_from_middleware_with_args
signed_cookies = decorator_from_middleware_with_args(SignedCookiesMiddleware)

@signed_cookies(salt='foo')
def foo(request, ...):
    ...

######
