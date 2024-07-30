from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    importance = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
