from django import forms
from drsch.models import *
from reports.models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class AddReport(forms.ModelForm):
	class Meta:
		model = ReportSent
		fields = ['report_topic', 'file', 'comment']
		'''widgets = {
			'report_topic': forms.HiddenInput(),
		}'''

class AddClass(forms.ModelForm):
	class Meta:
		model = Class
		fields = ['subject', 'class_form', 'course']

class AddTopic(forms.ModelForm):
	#class_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
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

	def __init__(self, *args, **kwargs):
		super(AddGrade, self).__init__(*args, **kwargs)
		self.fields['file'].required=False

	class Meta:
		model = ReportSent
		fields = '__all__'
		"""widgets = {
			'user': forms.HiddenInput(),
			'report_topic': forms.HiddenInput(),
			'file': forms.ClearableFileInput(),
			'comment': forms.HiddenInput(),
				
		}"""

	def save(self, commit=True):
		self.instance.grade = self.cleaned_data['grade']
		return super(AddGrade, self).save(commit=commit)

"""class AddGrade(forms.Form):
	grade = forms.FloatField()

	def save(self, commit=True):
		reportsent = ReportSent.objects.get('grade')
		reportsent.grade = self.cleaned_data["grade"]

		if commit:
			reportsent.save()
		return ReportSent"""
"""class ChooseClassForm(forms.ModelForm):
	class Meta:
		model = ClassForm
		fields = '__all__'"""