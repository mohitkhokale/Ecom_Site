from django.db import models

# Create your models here.
class Dashboard(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.name
