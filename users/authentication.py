from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser
import json

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        body = request.body

        if body:
            try:
                data = json.loads(body.decode('utf-8'))
                auth_token = data.get('token')
                if not auth_token:
                    return None
                try:
                    user = CustomUser.objects.get(authentication_token=auth_token)
                except CustomUser.DoesNotExist:
                    raise AuthenticationFailed('Invalid token')
            except Exception as e:
                raise AuthenticationFailed(f'{e}')

        else:
            return None
        
        return (user, None)
