from django.db import models


class Task(models.Model):
    content = models.CharField('内容', max_length=100)
