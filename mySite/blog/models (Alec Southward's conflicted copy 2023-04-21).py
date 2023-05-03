from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40, default='')
    content = models.CharField(max_length=600, default='')
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title