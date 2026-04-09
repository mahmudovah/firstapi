from django.urls import path, include
from blog import views
from rest_framework.routers import SimpleRouter
from blog.views import PostViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]