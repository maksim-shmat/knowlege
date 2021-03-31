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

######
