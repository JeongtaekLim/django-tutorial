import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class SignupQuestioner(models.Model):
    name = models.CharField(max_length=100)
    CHOICES = [('남', '남'), ('여', '여')]
    sex = models.CharField(choices=CHOICES, max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class SignupAnswerer(models.Model):
    name = models.CharField(max_length=100)
    CHOICES = [('남', '남'), ('여', '여')]
    sex = models.CharField(choices=CHOICES, max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

