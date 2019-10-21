from dependencies.contrib.rest_framework import model_view_set
from dependencies import Injector, Package, operation, this
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from example.serializers.user import UserSerializer

implemented = Package("example.implemented")
functions = Package("example.functions")


@model_view_set
class SignUpModelViewSet(Injector):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    sign_up = implemented.SignUp.register_user

    @operation
    def create(request, validated_data, sign_up):
        result = sign_up.run(validated_data, request)
        return result.value
