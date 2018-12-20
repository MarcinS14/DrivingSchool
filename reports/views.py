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
from django.db.models import Q

# Create your views here.

@login_required
def report(request, reporttopic_id):
	if request.method == 'POST':
		temp = ReportTopic.objects.get(id=reporttopic_id)
		add_report_form = AddReport(request.POST, request.FILES)

		if add_report_form.is_valid():
			instance = add_report_form.save(commit=False)
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


@login_required
def classes(request, reporttopic_id):
	queryset = ReportTopic.objects.filter(class_id_id=reporttopic_id)
	context = {
		"queryset": queryset,
		"reporttopic_id": reporttopic_id
	}
	return render(request, "reports/classes.html", context)


@user_passes_test(lambda user: user.is_teacher)
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
		instance = add_report_topic.save(commit=True)
		instance.save()
		return redirect(reverse_lazy('topics', kwargs = {'reporttopic_id': temp.id}))

	return render(request, "reports/topics.html", context)


@user_passes_test(lambda user: user.is_teacher)
def delete_topic(request, reporttopic_id):
    reporttopic = ReportTopic.objects.get(id=reporttopic_id)
    reporttopic.delete()
    return redirect(reverse_lazy('topics', kwargs = {'reporttopic_id': reporttopic.class_id.id}))


@user_passes_test(lambda user: user.is_teacher)
def delete_class(request, class_id):
	class_class = Class.objects.filter(id=class_id)
	class_class.delete()
	return redirect(reverse_lazy('profile'))


@user_passes_test(lambda user: user.is_teacher)
def report_teacher(request, report_id):
	queryset = ReportSent.objects.filter(report_topic_id=report_id)

	context = {
			"queryset": queryset,
			"report_id": report_id,
		}

	return render(request, "reports/report_teacher.html", context)


@user_passes_test(lambda user: user.is_teacher)
def report_teacher_modal(request, report_id):
	if request.method == 'POST':
		temp = ReportSent.objects.get(id=report_id)
		add_grade_form = AddGrade(request.POST, request.FILES)
		

		if add_grade_form.is_valid():
			temp.user = temp.user
			temp.report_topic = temp.report_topic
			temp.file = temp.file
			comment = add_grade_form.cleaned_data.get("comment")
			grade = add_grade_form.cleaned_data.get("grade")
			temp.grade = grade
			temp.comment = comment
			temp.save()
			return redirect(reverse_lazy('report_teacher', kwargs={'report_id': temp.report_topic.id}))

	else:
		temp = ReportSent.objects.get(id=report_id)
		add_grade_form = AddGrade(initial={
											'user': temp.user,
											'report_topic': temp.report_topic,
											'date': temp.date,
											})
	context = {
			"add_grade_form": add_grade_form,
			"report_id": report_id,
		}

	return render(request, "reports/report_teacher_modal.html", context)

@login_required
def report_student(request, username):
	queryset = ReportSent.objects.filter(user=username)
	context = {
			"queryset": queryset,
			"username": username,
		}

	return render(request, "reports/report_student.html", context)