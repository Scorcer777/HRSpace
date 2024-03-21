from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import LoginSerializer
from apps.users.models import CustomUser


class CustomAuthToken(GenericAPIView):

    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            201: openapi.Response(description='Successful login', schema=openapi.Schema(type='object', properties={'auth_token': openapi.Schema(type='string', description='JWT token for authentication')})),
            401: openapi.Response(description='Unable to log in with provided credentials', schema=openapi.Schema(type='object', properties={'detail': openapi.Schema(type='string', description='Error message')}))
        }
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'auth_token': token.key})
        except CustomUser.DoesNotExist:
            pass

        return Response(
            {'detail': 'Unable to log in with provided credentials.'},
            status=status.HTTP_401_UNAUTHORIZED
        )


obtain_auth_token = CustomAuthToken.as_view()
