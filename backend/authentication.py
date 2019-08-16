from rest_framework import authentication
from rest_framework import exceptions
from rest_framework_api_key.models import APIKey


class AccessKeyAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        access_key = request.GET.get("key", None)
        print(access_key)
        if not access_key:
            raise exceptions.NotFound("Access key not provided.")
        try:
            user = APIKey.objects.get(hashed_key=access_key)
        except APIKey.DoesNotExist:
            raise exceptions.PermissionDenied("No User found with the access key")
        except ValueError:
            raise exceptions.ValidationError("Badly formed hexadecimal UUID string")

        return (user, None)
