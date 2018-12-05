from django.conf.urls import url
from . import views
from django.contrib.auth.views import auth_logout

urlpatterns=[
    url(r'^login/$',views.userLogin,name="userLogin"),
    url(r'^register/$',views.userRegister,name="userRegister"),
    url(r'^logout/$',views.logout,name="userLogout"),
]