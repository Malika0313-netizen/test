from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    phone = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.name

