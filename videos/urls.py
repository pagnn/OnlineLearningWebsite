from django.conf.urls import url,include
from .views import VideoListView,VideoDetailView,VideoCreateView,VideoUpdateView,VideoDeleteView

urlpatterns = [
    url(r'^$', VideoListView.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(),name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', VideoUpdateView.as_view(),name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', VideoDeleteView.as_view(),name='detele'),
    url(r'^video/create/$', VideoCreateView.as_view(),name='create'),
]
