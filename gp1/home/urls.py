
from django.conf.urls import include, url

from .views import HomePage

urlpatterns = [
    url(r'^index/', HomePage.as_view(), name='index'),
    url(r'^index/image-process', HomePage.as_view(), name='image_process')
]