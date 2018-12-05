from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.Article,name="Article"),
    url(r'^manage/$',views.manage,name="manage"),
    url(r'(?P<id>\d)/$',views.articleContent,name="content"),
]