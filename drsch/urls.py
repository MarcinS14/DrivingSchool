from django.urls import path
from drsch import views
from django.conf.urls import url

urlpatterns = [
	#path('', views.home, name='home'),

	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
	#path('signup/', views.SingUp.as_view(), name='signup'),
	url(r'^signup/$', views.SignUp.as_view(), name='signup'),
]