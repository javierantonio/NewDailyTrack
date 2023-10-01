from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Journal(models.Model):
    user = models.ForeignKey('registration.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    isStarred = models.BooleanField(default=False)
    sharedWith = models.ManyToManyField(User, blank=True, related_name='sharedWith')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title