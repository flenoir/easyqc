from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid


# Create your models here.

class Asset(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    filename = models.CharField(blank=True, max_length=150)
    file = models.FileField(upload_to='files/')
    data = JSONField(blank=True, null=True)

    def __str__(self):
        return self.filename

    # def save(self):
    #     pass

    # surcharge de la methode delete
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
