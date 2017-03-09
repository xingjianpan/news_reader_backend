from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from wall import views
from .views import PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^wall/', include(router.urls)),
]
