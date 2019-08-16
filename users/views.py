from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from users.serializers import UserSerializer
from django.contrib.auth import authenticate
from users.models import User
from django.contrib.auth import logout
from rest_framework_api_key.models import APIKey

from users.models import User
from rest_framework.authtoken.models import Token


class UserLogin(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            user_data = {}
            user_data['email'] = user.__str__()
            user_data['api_key'] = User.objects.get(email=user).api_key
            user_data['token'] = token[0].__str__()
            return Response({'user': user_data, 'success': True},
                            status=status.HTTP_200_OK)
        else:
            return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


class CreateUser(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, format=None):

        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            # User.objects.create_user(
            #     serialized.save()
            # )
            if User.objects.filter(email=request.data.get('email')).exists():
                return Response({'message': "This email id is already registred", 'success': False},
                                status=status.HTTP_200_OK)
            api_key, key = APIKey.objects.create_key(name=request.data.get('email'))
            User.objects.create_user(email=request.data.get('email'), username=request.data.get('username'),
                                     password=request.data.get('password'), api_key=key)

            return Response({'user': serialized.data, 'success': True}, status=status.HTTP_201_CREATED)

        else:
            return Response({'message': serialized._errors.__str__(), 'success': False}, status=status.HTTP_200_OK)


#
# def logout_view(request):
# #     logout(request)


class Logout(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, format=None):
        # simply delete the token to force a login
        logout(request)
        # request.user.auth_token.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
