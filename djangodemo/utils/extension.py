from rest_framework.response import Response
from django.conf import settings
from rest_framework import authentication, exceptions, serializers


import jwt


def JsonResponse(code: int, data: dict or list = None, info: str = "ok", status=None):
    """格式化返回"""
    return Response(
        {
            "code": code,
            "data": data if data is not None else {},
            "info": info,
        },
        status=status if status else code,
    )


def get_userid_from_jwt_header(request):
    token = request.META.get("HTTP_MBD_T", None)
    res = decode_jwt(token)
    return res.get("user_id")


def encode_jwt(user_id, expired_at):
    return jwt.encode(
        {"user_id": user_id, "expired_at": expired_at},
        settings.SECRET_KEY,
        algorithm="HS256",
    )


def decode_jwt(token):
    try:
        res = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except:  # noqa
        return {}

    expired_at = res.get("expired_at", 0)
    if expired_at < int(time.time()):
        return {}
    else:
        return res


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        jwt_user_id = get_userid_from_jwt_header(request)
        # print("jwt user_id: {}".format(jwt_user_id))
        # if not jwt_user_id:
        # raise exceptions.AuthenticationFailed("验证失败")
        return 1, None
