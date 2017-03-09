from rest_framework import serializers
from .models import Post
from django.views.decorators.csrf import csrf_exempt


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'owner')
