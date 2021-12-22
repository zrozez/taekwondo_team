from django.db import models


class News(models.Model):
    name = models.TextField()
    information = models.TextField()
    images = models.URLField(max_length=999)