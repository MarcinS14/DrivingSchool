from django.urls import path
from drsch import views
from reports import views
from django.conf.urls import url

urlpatterns = [
	url(r'^report/(?P<reporttopic_id>[\w ]+)/$', views.report, name='report'),
	url(r'^classes/(?P<reporttopic_id>[\w ]+)/$', views.classes, name='classes'),
	url(r'^topics/(?P<reporttopic_id>[\w ]+)/$', views.topics, name='topics'),
	url(r'^delete_topic/(?P<reporttopic_id>[\w ]+)/$', views.delete_topic, name='delete_topic'),
	url(r'^delete_class/(?P<class_id>[\w ]+)/$', views.delete_class, name='delete_class'),
	url(r'^report_teacher/(?P<report_id>[\w ]+)/$', views.report_teacher, name='report_teacher'),
	url(r'^report_teacher_modal/(?P<report_id>[\w ]+)/$', views.report_teacher_modal, name='report_teacher_modal'),
	url(r'^report_student/(?P<username>[\w ]+)/$', views.report_student, name='report_student'),
		
	
		
]	
