from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.

class User(AbstractUser):
	is_teacher = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

