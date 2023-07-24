from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CMSUser


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        validated_token = self.get_validated_token(raw_token)

        if validated_token is None:
            return None

        user_id = validated_token['user_id']
        try:
            user = CMSUser.objects.get(pk=user_id)
            return user, validated_token
        except CMSUser.DoesNotExist:
            return None
