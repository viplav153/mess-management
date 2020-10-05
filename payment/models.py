from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subs = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    thali = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Info(models.Model):
    subs = models.IntegerField(default=1)
    pub_date = models.DateTimeField(auto_now_add=True)
    subscribed_by = models.ForeignKey(User, on_delete=models.CASCADE)
