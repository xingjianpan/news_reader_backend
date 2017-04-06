from rest_framework import serializers
from .models import Article

from django.contrib.auth import get_user_model
User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    link = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'headline', 'fly_title', 'alternativename',
            'content_dirty', 'content_clean', 'category', 'source', 'pub_date',
            'create_date', 'source_url', 'spider', 'project',
            'link', 'owner')
