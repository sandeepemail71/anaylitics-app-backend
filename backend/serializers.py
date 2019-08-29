from django.contrib.auth.models import User, Group
from backend.models import UserData
from rest_framework import serializers


class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ['page_url', 'ip_address', 'country', 'browser', 'screen_resolution', 'date', 'browser_version', 'os',
                  'currency',
                  'city', 'region', 'latitude', 'longitude', 'os_version', 'platform_type', 'platform_vendor']
