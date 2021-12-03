from django.db import models

# Create your models here.

class stack(models.Model):
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    answerTo=models.CharField(max_length=100)
    tage=models.CharField(max_length=50)

    def __str__(self):
        return self.question