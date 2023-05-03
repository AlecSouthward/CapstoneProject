from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """The model for a Post that can be
        created by an admin and seen by users on the site.
    """
    content = models.CharField(max_length=800, default='')
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.title