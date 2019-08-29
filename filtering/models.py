from django.db import models


class ImgSave(models.Model):
    image = models.FileField(upload_to="images", blank=True)
    image_f = models.FileField(upload_to="images", blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)