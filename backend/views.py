from django.contrib.auth.models import User, Group
from backend.models import UserData
from users.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from backend.serializers import UserSerializer, GroupSerializer, UserDataSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, _
from rest_framework import status
from django.db.models import Count
from rest_framework.authtoken.models import Token
from django.http import Http404


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


class UserDataSet(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        print(request.META.get('HTTP_API_KEY'), '____________key')
        api_key = request.META.get('HTTP_API_KEY')
        serializer = UserDataSerializer(data=request.data)
        print(serializer.is_valid())
        serializer.validated_data['user'] = User.objects.get(api_key=api_key).email

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserDataSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = UserData.objects.all()
        serializer = UserDataSerializer(queryset, many=True)
        return Response(serializer.data)


class GetTop10PagesSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token).user.email
        queryset = UserData.objects.values('page_url').filter(user=user).annotate(
            dcount=Count('page_url')).order_by('dcount').reverse()
        return Response(queryset[:10])


class GetTop10CountriesSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token).user.email
        queryset = UserData.objects.values('country').filter(user=user).annotate(dcount=Count('country')).order_by(
            'dcount').reverse()
        return Response(queryset[:10])


class GetTop10BrowsersSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token).user.email
        queryset = UserData.objects.values('browser').filter(user=user).annotate(dcount=Count('browser')).order_by(
            'dcount').reverse()
        return Response(queryset[:10])


class GetTop10ScreenResolutionsSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token).user.email
        queryset = UserData.objects.values('screen_resolution').filter(user=user).annotate(
            dcount=Count('screen_resolution')).order_by(
            'dcount').reverse()
        return Response(queryset[:10])



class GetFilterDataSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        key_browser = request.GET.get('browser')
        key_country = request.GET.get('country')
        key_date_range = request.GET.get('key_date_range')

        user = Token.objects.get(key=token).user.email

        queryset = UserData.objects.filter(user=user)

        if key_browser:
            queryset = queryset.filter(browser=key_browser)
        if key_country:
            queryset = queryset.filter(country=key_country)
        if key_date_range:
            queryset = queryset.filter(date__range=key_date_range)

        serializer = UserDataSerializer(queryset, many=True)
        return Response(serializer.data)
