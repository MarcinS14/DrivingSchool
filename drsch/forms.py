"""from django import forms
from django.contrib.auth.forms import UserCreationForm
from drsch.models import User

class UserCreateForm(UserCreationForm):
		email = forms.EmailField(required=True)

		class Meta:
			model = User
			fields = ("username",
					  "first_name",
					  "last_name",
					  "email",
						)

		def save(self, commit=True):
			user = super(UserCreateForm, self).save(commit=False)
			user.email = self.cleaned.data["email"]
			user.first_name = self.cleaned.data["first_name"]
			user.last_name = self.cleaned.data["last_name"]

			if commit:
				user.save()
			return user"""