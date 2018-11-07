from django.db import models
from drsch.models import *

# Create your models here.
 
 #class Report(models.Model):
 #	report_name = models.CharField(max_length=30)
 #	report_date = models.DateField(auto_now_add=True)
 #	user = models.ForeignKey(User, default=1)
 	
 class Subject(models.Model):
 	subject_name = models.CharField(max_length=30)

 class ClassForm(models.Model):
 	class_form_name = models.CharField(max_length=30)

 class Class(models.Model):
 	subject = models.ForeignKey(Subject)
 	class_form = models.ForeignKey(ClassForm)
 	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
 	class_name = models.CharField(max_length=30)

 class ReportTopic(models.Model):
 	class_id = models.ForeignKey(Class)
 	topic = models.CharField(max_length=30)
 	text = models.CharField(max_length=300)

 class ReportSent(models.Model):
 	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
 	report_topic = models.ForeignKey(ReportTopic)
 	file = models.CharField(max_length=30)
 	date = models.DateField(auto_now_add=True)
 	grade = models.FloatField()
 	comment = models.CharField()
 
 class StudentClass(models.Model):
 	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
 	class_id = models.ForeignKey(Class)
 
 class NewStudent(models.Model):
 	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
 	report_sent = models.ForeignKey(ReportSent)
 	