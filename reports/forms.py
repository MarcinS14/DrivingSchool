from django import forms
from drsch.models import *
from reports.models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class AddReport(forms.ModelForm):
	class Meta:
		model = ReportSent
		fields = ['report_topic', 'file']
		widgets = {
			'report_topic': forms.HiddenInput(),
		}


class AddClass(forms.ModelForm):
	class Meta:
		model = Class
		fields = ['subject', 'class_form', 'course']


class AddTopic(forms.ModelForm):
	class Meta:
		model = ReportTopic
		fields = '__all__'
		widgets = {
			'class_id': forms.HiddenInput(),
		}


class AddSubject(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'


class AddGrade(forms.ModelForm):

	class Meta:
		CHOICES = (
		('2','2'),
		('2.5','2.5'),
		('3','3'),
		('3.5','3.5'),
		('4','4'),
		('4.5','4.5'),
		('5','5'),
		)
		model = ReportSent
		exclude = ['file']
		widgets = {
			'user': forms.HiddenInput(),
			'report_topic': forms.HiddenInput(),
			'grade': forms.Select(choices=CHOICES),		
		}

	def save(self, commit=True):
		self.instance.grade = self.cleaned_data['grade']
		self.instance.comment = self.cleaned_data['comment']
		return super(AddGrade, self).save(commit=commit)
