from django.db import models

# Create your models here.

class HookReg(models.Model):
    to_url = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    secret = models.CharField(max_length=200, default='default')
    def __str__(self):
        return self.to_url
