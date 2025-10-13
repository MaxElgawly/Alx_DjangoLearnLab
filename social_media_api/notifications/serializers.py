from .models import Post, Comment, Like
from rest_framework import serializers
from .models import Notification

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Notification
        fields = [
            'id', 'actor_username', 'recipient_username',
            'verb', 'timestamp', 'is_read'
        ]