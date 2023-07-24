from django.db import models


class CMSUser(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=100, blank=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CMSUser, on_delete=models.CASCADE, related_name='posts')
    is_public = models.BooleanField(default=True)


class Like(models.Model):
    user = models.ForeignKey(CMSUser, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
