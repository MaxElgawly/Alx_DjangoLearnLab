from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'author_username', 'created_at', 'updated_at']

class PostListSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'author_username', 'content', 'comments_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'author_username', 'comments_count', 'created_at', 'updated_at']

class PostDetailSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'author_username', 'content', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'author_username', 'comments', 'created_at', 'updated_at']
