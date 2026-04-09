from blog.serializers import PostSerializer, CategorySerializers
from blog.models import Post, Category
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]