from rest_framework import serializers
from .models import CMSUser, Post, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('owner',)

    def get_likes_count(self, post):
        return post.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
