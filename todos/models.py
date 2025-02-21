from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# default user when signin- it needs as system wants it to be defined, can defined manually also 

def get_default_user():
    return User.objects.first().id

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created',  auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)

    def __str__(self):
        return self.title

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='pics/', blank=True, null=True)