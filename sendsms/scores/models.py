from django.db import models


# Create your models here.
class Score(models.Model):
    result = models.PositiveIntegerField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.result)
