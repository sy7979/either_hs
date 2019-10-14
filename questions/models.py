from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    content_a = models.CharField(max_length=100)
    content_b = models.CharField(max_length=100)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    pick = models.IntegerField()
    user_name = models.CharField(max_length=50)

    # count1
    # count2

