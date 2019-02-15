from django.conf.urls import url
from django.contrib import admin
from blog import views 



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about/',views.about),
    url(r'^kontak/',views.kontak),
    url(r'^blog/',views.blog),
]
