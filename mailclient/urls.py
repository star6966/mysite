from django.conf.urls import patterns, url

from mailclient import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#ex: /mailclient/5/
	url(r'(?P<user_id>\d+)/$', views.inbox, name='inbox'),
	#ex: /mailclient/5/outbox/
	url(r'(?P<user_id>\d+)/outbox/$', views.outbox, name='outbox'),
	#ex: /mailclient/5/newMessage/
	url(r'(?P<user_id>\d+)/newMessage/$', views.new_message, name='create'),
)