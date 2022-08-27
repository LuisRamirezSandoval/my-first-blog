from django.conf import settings
from django.db import models
from django.utils import timezone


class PostInt(models.Model):
    text1 = models.IntegerField()
    text2 = models.IntegerField()
    text3 = models.IntegerField()

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.text1
