from django.urls import path
from drsch import views
from django.conf.urls import url

urlpatterns = [
	#path('', views.home, name='home'),

	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
	#path('signup/', views.SingUp.as_view(), name='signup'),
	url(r'^signup/$', views.SignUp.as_view(), name='signup'),
	#url(r'^signup_student/$', views.SignUpStudent.as_view(), name='signup_student'),
	#url(r'^signup_teacher/$', views.SignUpTeacher.as_view(), name='signup_teacher'),
	#url(r'^password_reset_form/$', views.passwordresetform, name='passwordresetform'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^admin/$', views.admin, name='admin'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^update_user/(?P<username>[\w ]+)/$', views.update_user, name='update_user'),
	url(r'^delete_user/(?P<username>[\w ]+)/$', views.delete_user, name='delete_user'),
	
		
]	