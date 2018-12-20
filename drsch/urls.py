from django.urls import path
from drsch import views
from django.conf.urls import url

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^signup/$', views.SignUp.as_view(), name='signup'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^admin/$', views.admin, name='admin'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^update_user/(?P<username>[\w ]+)/$', views.update_user, name='update_user'),
	url(r'^delete_user/(?P<username>[\w ]+)/$', views.delete_user, name='delete_user'),
	url(r'^student/$', views.student, name='student'),
	url(r'^teacher/$', views.teacher, name='teacher'),
	
		
]	