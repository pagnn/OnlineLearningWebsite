from django.conf.urls import url,include
from .views import SearchView

urlpatterns = [
    url(r'^$', SearchView.as_view(),name='default'),

]