from django.db import models, migrations
from django.contrib.auth.hashers import make_password

def initial_users(apps, schema_editor):
	user = apps.get_model("drsch", "User")

	user(username='admin',
		email='admin@gmail.com',
		password=make_password('admin'),
		is_admin=True,
		).save()


class Migration(migrations.Migration):
	dependencies = [
		('drsch','0001_initial'),
		]

	operations = [
		migrations.RunPython(initial_users)
		]