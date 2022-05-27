from djangodemo.utils.extension import JsonResponse, JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes


@api_view(("GET",))
@authentication_classes([JWTAuthentication])
def index(request):
    return JsonResponse(code=200, info="ok")
