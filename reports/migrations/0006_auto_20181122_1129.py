# Generated by Django 2.1 on 2018-11-22 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20181121_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporttopic',
            name='class_id',
        ),
        migrations.AlterField(
            model_name='class',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reportsent',
            name='report_topic',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='ReportTopic',
        ),
    ]
