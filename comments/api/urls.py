from django.conf.urls import url
from .views import CommentsListAPIView,CommentsCreateAPIView,CommentsUpdateAPIView
urlpatterns = [
    url(r'^$', CommentsListAPIView.as_view(),name='list'),
    url(r'^create/$', CommentsCreateAPIView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$', CommentsUpdateAPIView.as_view(),name='update'),
]