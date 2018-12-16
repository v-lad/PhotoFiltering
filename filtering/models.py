from django.db import models


class ImgSave(models.Model):
    image = models.FileField(upload_to="images", null=True, blank=True)
