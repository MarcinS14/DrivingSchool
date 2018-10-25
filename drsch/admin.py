"""from django.contrib import admin
from drsch.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.

class UsersAdmin(UserAdmin):
	fieldsets = ((None, {'fields': ('username', 'password')}),
		(_('Personal_info'), {'fields': ('is_active', 'is_staff', 'is_superuser',
										 'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
		)
	search_fields = ['username']
	ordering = ['username']

admin.site.register(User, UserAdmin)"""