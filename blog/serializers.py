from rest_framework import serializers
from blog.models import Category, Post
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'date_joined']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'posts_count']


class PostSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all, source='category',write_only=True)
    author = UserSerializers(read_only=True)
    #category = CategorySerializers(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category_id', 'body', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user
        return super().create(validated_data)