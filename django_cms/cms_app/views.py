from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import CMSUser, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from .permissions import  IsOwner, IsAuthenticated, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = CMSUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.filter(Q(is_public=True) | Q(owner=request.user.id))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        request_data = request.data
        if Like.objects.filter(user=user_id, post=request_data.get("post")).exists():
            return Response({'message': 'You already liked on this post.'},
                            status=status.HTTP_200_OK)
        else:
            request_data.update({'user': user_id})
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Post created successfully.'}, status=status.HTTP_201_CREATED)
