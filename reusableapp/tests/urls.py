from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url(r'^o/', include(('myapp.urls', 'myapp'), namespace='myapp')),
]