from django.conf.urls import url
 
from . import view1
 
urlpatterns = [
    url(r'^$', view1.hello),
]