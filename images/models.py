from django.db import models


class Images(models.Model):
    name = models.TextField()
    images = models.URLField(max_length=999)