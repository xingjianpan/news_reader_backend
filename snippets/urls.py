from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^/$', views.api_root),
    url(r'^snippets/$',
        views.PublicSnippetList.as_view(),
        name='snippet-list'),
    url(r'^mysnippets/$',
        views.UserSnippetList.as_view(),
        name='mysnippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^user-snippets/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^user-snippets/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
])
