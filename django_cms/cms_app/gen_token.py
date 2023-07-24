from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import CMSUser
from rest_framework import viewsets, status


class GenerateTokenViewSet(viewsets.ViewSet):
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = CMSUser.objects.get(name=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({'access_token': access_token,
                                 "refresh_token": str(refresh)},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)