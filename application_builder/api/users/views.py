from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer
from apps.users.models import CustomUser


class CustomAuthToken(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
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
