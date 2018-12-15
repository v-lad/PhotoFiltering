from django.db import models
from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='/live-static-files/media-root/images')


# Create your models here.
class ImgSave(models.Model):
    image = models.FileField(upload_to="images", null=True, blank=True)
