from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created',  auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)

    def __str__(self):
        return self.title 

