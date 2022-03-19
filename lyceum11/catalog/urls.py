
from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)$', views.item_detail),
    url(r'^$', views.item_list)
]