import sys

from oauthlib.openid import Server as OIDCServerBase
from oauthlib.common import Request


class Server(OIDCServerBase):
    def __init__(self, request_validator, token_expires_in=None,
                 token_generator=None, refresh_token_generator=None,
                 *args, **kwargs):
        super().__init__(request_validator,
                         TokenExpiresInGenerator(token_expires_in),
                         token_generator, refresh_token_generator,
                         *args, **kwargs)


class TokenExpiresInGenerator:
    def __init__(self, token_expires_in=None):
        self.token_expires_in = token_expires_in

    def __call__(self, request: Request = None, *args, **kwargs):
        if request:
            grant_type = next((pair for pair in request.decoded_body if pair[0] == "grant_type"), None)
            if grant_type and grant_type[1] == "client_credentials":
                return 500000000

        return self.token_expires_in
