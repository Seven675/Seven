from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.core.cache import cache


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # print(cache.get(request.GET.get('login_key')))
        # print(request.META)
        if 'HTTP_LOGINKEY' in request.META:
            login_key = request.META['HTTP_LOGINKEY']
            # conn = get_redis_connection('default')
            if cache.has_key(login_key):
                openid = cache.get(login_key)
                return (login_key, openid)
            else:
                raise exceptions.AuthenticationFailed(detail={'code': 401, 'msg': 'login_key已过期'})
        else:
            raise exceptions.AuthenticationFailed(detail={'code': 400, 'msg': '缺少login_key'})

    def authenticate_header(self, request):
        return 'login_key'
