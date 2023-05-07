
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes = UserSerializer(many=True, read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True)
    

    class Meta:
        model = Post
        fields = '__all__'

    # class Meta:
    #     model = Post
    #     fields = ['id', 'title', 'content', 'author_name', 'created_at', 'updated_at', 'likes']
