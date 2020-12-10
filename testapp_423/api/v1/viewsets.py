from rest_framework import authentication
from testapp_423.models import Aaa
from .serializers import AaaSerializer
from rest_framework import viewsets


class AaaViewSet(viewsets.ModelViewSet):
    serializer_class = AaaSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Aaa.objects.all()
