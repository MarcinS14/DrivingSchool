from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from drsch.forms import *
from reports.forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from itertools import chain
from django.http import Http404
from django.utils.decorators import method_decorator
from drsch.models import User
from reports.models import *
from pprint import pprint

# Create your views here.

def login(request):

	return render(request, 'login.html')


class SignUp(generic.CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


def contact(request):
	contact_form = Contact(request.POST or None)

	context = {
        "title": "Contact",
        "contact_form": contact_form,
    }
	if contact_form.is_valid():
		sender = contact_form.cleaned_data.get("sender")
		subject = contact_form.cleaned_data.get("subject")
		from_email = contact_form.cleaned_data.get("email")
		message = contact_form.cleaned_data.get("message")
		message = 'Sender:  ' + sender + '\nFrom:  ' + from_email + '\n\n' + message
		send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently=True)
		success_message = "Message has been sent" 
		messages.success(request, success_message)

		return redirect(reverse_lazy('contact'))

	return render(request, "accounts/contact.html", context)


@login_required
def profile(request):
	if request.user.is_admin:
		return redirect(reverse_lazy('admin'))
	elif request.user.is_teacher:
		return redirect(reverse_lazy('teacher'))

	return redirect(reverse_lazy('student'))


@user_passes_test(lambda user: user.is_admin)
def admin(request):
	add_user_form = AddUser(request.POST or None)
	queryset = User.objects.all()

	search = request.GET.get("search")
	if search:
		queryset = queryset.filter(username__icontains=search)

	context = {
		"title": "Admin",
		"add_user_form": add_user_form,
		"queryset": queryset,
		}

	if add_user_form.is_valid():
		instance = add_user_form.save(commit=False)
		passwd = add_user_form.cleaned_data.get("password")
		instance.password = make_password(password=passwd, salt='salt',)

		instance.save()
		reverse_lazy('profile')

	return render(request, "accounts/admin_mainsite.html", context)


@user_passes_test(lambda user: user.is_admin)
def update_user(request, username):
    user = User.objects.get(username=username)
    data_dict = {'username': user.username, 'email': user.email}
    update_user_form = EditUser(initial=data_dict, instance=user)

    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    context = {
        "title": "Edit",
        "update_user_form": update_user_form,
        "path": path,
        "redirect_path": redirect_path,
    }

    if request.POST:
        user_form = EditUser(request.POST, instance=user)

        if user_form.is_valid():
            instance = user_form.save(commit=False)
            passwd = user_form.cleaned_data.get("password")

            if passwd:
                instance.password = make_password(password=passwd,
                                                  salt='salt', )
            instance.save()

            return redirect(reverse_lazy('profile'))

    return render(request, "accounts/edit_user.html", context)


@user_passes_test(lambda user: user.is_admin)
def delete_user(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect(reverse_lazy('profile'))


@user_passes_test(lambda user: user.is_teacher)
def teacher(request):
	add_class_form = AddClass(request.POST or None)
	add_subject_form = AddSubject(request.POST or None)
	queryset = Class.objects.filter(user=request.user) 

	context = {
		"title": "Teacher",
		"add_class_form": add_class_form,
		"add_subject_form": add_subject_form,
		"queryset": queryset,

	}

	if add_class_form.is_valid():
		class_name = add_class_form.cleaned_data.get("class_name")
		instance = add_class_form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect(reverse_lazy('profile'))

	if add_subject_form.is_valid():
		subject_name = add_subject_form.cleaned_data.get("subject_name")
		instance = add_subject_form.save(commit=False)
		instance.save()
		return redirect(reverse_lazy('profile'))

	return render(request, "accounts/teacher_mainsite.html", context)


@login_required
def student(request):
	queryset = Class.objects.all()
	context = {
		"queryset": queryset,
		"title": request.user,
	}
	return render(request, "accounts/student_mainsite.html", context)
