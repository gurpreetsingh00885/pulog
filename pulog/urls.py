
from django.conf.urls import url
from django.contrib import admin
from score.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<teams>[\w-]{2,2})/$', index.as_view())
]
