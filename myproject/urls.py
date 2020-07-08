from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from boards import views

urlpatterns = [
	path('', views.home, name='home'),
	url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
	url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
]
