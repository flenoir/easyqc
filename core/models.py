from django.db import models


# Create your models here.

class Asset(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True, null=False)
    filename = models.CharField(max_length=150)
    file = models.FileField(upload_to='assets/files/')

    def __str__(self):
        return self.filename
