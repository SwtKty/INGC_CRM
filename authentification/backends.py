import jwt
from django.conf import settings

from rest_framework import authentication, exceptions


class JWTAuthentication(authentication.BasicAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split('')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
        except expression as identifier:
            pass


        return super().authenticate(request)