from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_home'),
    url(r'complete/?$', views.complete),
]