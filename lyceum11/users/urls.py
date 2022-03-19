from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'users/$', views.user_list),
    url(r'^users/(?P<id>[0-9]+)$', views.user_detail),
    url(r'signup/$', views.signup),
    url(r'profile/$', views.profile),
]