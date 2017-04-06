from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^articles/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(),
        name='article_detail'),
]
