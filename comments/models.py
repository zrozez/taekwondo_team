from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.TextField()
    information = models.TextField(null=True)