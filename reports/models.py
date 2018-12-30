from django.db import models
from drsch.models import *

# Create your models here.
 
def user_directory_path (instance, filename):
    return 'uploads/{0}/{1}/{2}'.format(instance.report_topic.topic, instance.user.username,  filename)

class Subject(models.Model):
    subject_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "{subject_name}".format(
            subject_name=self.subject_name)


class Class(models.Model):
    LABORATORY='LAB'
    PROJECT='PRO'
    CLASS="CLA"
    LECTURE="LEC"
    CLASS_FORM_CHOICES = (
        (LABORATORY, 'Laboratory'),
        (PROJECT, 'Project'),
        (CLASS, 'Class'),
        (LECTURE, 'Lecture'),
        )

    AUTOMATYKA1='EA-DI(01)'
    AUTOMATYKA2='EA-DI(02)'
    AUTOMATYKA3='EA-DI(03)'
    AUTOMATYKA4='EA-DI(04)'
    AUTOMATYKA5='EA-DI(05)'
    AUTOMATYKA6='EA-DI(06)'
    AUTOMATYKA7='EA-DI(07)'
    INFORMATYKA1='EF-DI(01)'
    INFORMATYKA2='EF-DI(02)'
    INFORMATYKA3='EF-DI(03)'
    INFORMATYKA4='EF-DI(04)'
    INFORMATYKA5='EF-DI(05)'
    INFORMATYKA6='EF-DI(06)'
    INFORMATYKA7='EF-DI(07)'
    COURSE_CHOICES = (
        (AUTOMATYKA1, 'EA-DI(01)'),
        (AUTOMATYKA2, 'EA-DI(02)'),
        (AUTOMATYKA3, 'EA-DI(03)'),
        (AUTOMATYKA4, 'EA-DI(04)'),
        (AUTOMATYKA5, 'EA-DI(05)'),
        (AUTOMATYKA6, 'EA-DI(06)'),
        (AUTOMATYKA7, 'EA-DI(07)'),
        (INFORMATYKA1, 'EF-DI(01)'),
        (INFORMATYKA2, 'EF-DI(02)'),
        (INFORMATYKA3, 'EF-DI(03)'),
        (INFORMATYKA4, 'EF-DI(04)'),
        (INFORMATYKA5, 'EF-DI(05)'),
        (INFORMATYKA6, 'EF-DI(06)'),
        (INFORMATYKA7, 'EF-DI(07)'),
        )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    class_form = models.CharField(max_length=10, choices=CLASS_FORM_CHOICES, default=LABORATORY)
    course = models.CharField(max_length=30, choices=COURSE_CHOICES, default=AUTOMATYKA1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{subject} {class_form} {course} {user}".format(
            subject=self.subject,
            class_form=self.class_form,
            course=self.course,
            user=self.user)


class ReportTopic(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    topic = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "{class_id} {topic}".format(
            class_id=self.class_id,
            topic=self.topic
            )


class ReportSent(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    report_topic = models.ForeignKey(ReportTopic, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path, max_length=200, blank=False)
    date = models.DateField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{user} {report_topic} {file} {date} {grade} {comment}".format(
            user=self.user,
            report_topic=self.report_topic,
            file=self.file,
            date=self.date,
            grade=self.grade,
            comment=self.comment)


    