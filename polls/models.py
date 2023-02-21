from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date_published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
