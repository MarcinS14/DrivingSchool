from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import *
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from itertools import chain
from django.http import Http404
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage

# Create your views here.

def report(request, reporttopic_id):
	if request.method == 'POST':
		temp = ReportTopic.objects.get(id=reporttopic_id)
		add_report_form = AddReport(request.POST, request.FILES)


		if add_report_form.is_valid():
			instance = add_report_form.save(commit=False)
			#instance.report = ReportSent.objects.get(report_topic=report_topic)
			instance.user = request.user
			instance.save()
			return redirect(reverse_lazy('student'))
	else:
		temp = ReportTopic.objects.get(id=reporttopic_id)
		add_report_form = AddReport(initial={'report_topic': temp,})

	context = {
			"add_report_form": add_report_form,
			"reporttopic_id": reporttopic_id,
		}

	return render(request, "reports/report.html", context)

def classes(request, reporttopic_id):
	queryset = ReportTopic.objects.filter(class_id_id=reporttopic_id)
	context = {
		"queryset": queryset,
		"reporttopic_id": reporttopic_id
	}
	return render(request, "reports/classes.html", context)

def topics(request, reporttopic_id):
	queryset = ReportTopic.objects.filter(class_id_id=reporttopic_id)
	temp = Class.objects.get(id=reporttopic_id)
	add_report_topic = AddTopic(request.POST or None, initial={'class_id':temp,})
	context = {
		"queryset": queryset,
		"add_report_topic": add_report_topic,
		"reporttopic_id": reporttopic_id,
	}

	if add_report_topic.is_valid():
		topic = add_report_topic.cleaned_data.get("topic")
		#class_id = add_report_topic.cleaned_data.get("class_id")
		instance = add_report_topic.save(commit=True)
		#instance.class_id = ReportTopic.objects.filter(id=class_id)
		instance.save()
		return redirect(reverse_lazy('profile'))


	return render(request, "reports/topics.html", context)

def delete_topic(request, reporttopic_id):
    reporttopic = ReportTopic.objects.filter(id=reporttopic_id)
    reporttopic.delete()
    return redirect(reverse_lazy('profile'))

def delete_class(request, class_id):
	class_class = Class.objects.filter(id=class_id)
	class_class.delete()
	return redirect(reverse_lazy('profile'))

def report_teacher(request):
	queryset = ReportSent.objects.all()
	#temp = ReportSent.objects.filter(id=report_id)
	#add_grade_form = AddGrade(request.POST or None, initial={'id':temp,})
	context = {
			"queryset": queryset,
			#"add_grade_form": add_grade_form,
			#"report_id": report_id,
		}

	'''if add_grade_form.is_valid():
		topic = add_grade_form.cleaned_data.get("topic")
		grade = add_grade_form.cleaned_data.get("grade")
		instance = add_grade_form.save(commit=True)
		instance.save()
		return redirect(reverse_lazy('report_teacher'))'''

	return render(request, "reports/report_teacher.html", context)

def report_teacher_modal(request, report_id):
	if request.method == 'POST':
		#queryset = ReportSent.objects.all()
		temp = ReportSent.objects.get(id=report_id)
		add_grade_form = AddGrade(request.POST, request.FILES)
		

		if add_grade_form.is_valid():
			temp.user = temp.user
			temp.report_topic = temp.report_topic
			temp.file = temp.file
			temp.comment = temp.comment
			
			#topic = add_grade_form.cleaned_data.get("topic")
			grade = add_grade_form.cleaned_data.get("grade")
			temp.grade = grade
			#file = add_grade_form.cleaned_data.get("file")
			#instance = add_grade_form.save(commit=False)
			#instance.save(force_update=True)
			temp.save()
			return redirect(reverse_lazy('report_teacher'))

	else:
		#queryset = ReportSent.objects.all()
		temp = ReportSent.objects.get(id=report_id)
		add_grade_form = AddGrade(initial={
											'user': temp.user,
											'report_topic': temp.report_topic,
											'file': temp.file,
											'date': temp.date,
											'comment': temp.comment,
											})
	context = {
			#"queryset": queryset,
			"add_grade_form": add_grade_form,
			"report_id": report_id,
		}

	return render(request, "reports/report_teacher_modal.html", context)