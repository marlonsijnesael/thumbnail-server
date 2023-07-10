import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image

FILE_EXTENSIONS = {
    ".jpg": "JPEG",
    ".jpeg": "JPEG",
    ".png": "PNG",
    ".gif": "GIF",
}


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


def scene_upload_to(instance, filename):
    return 'scenes/{filename}'.format(filename=filename)


# Database model for projects
class Project(models.Model):
    name = models.CharField(max_length=64)
    scene = models.FileField(upload_to=scene_upload_to)


# Database model for textures
class TextureImage(models.Model):
    title = models.CharField(
        max_length=80, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        image = Image.open(self.image)
        image.thumbnail((64, 64), Image.ANTIALIAS)
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension

        file_type = FILE_EXTENSIONS.get(thumb_extension, False)

        if not file_type:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, file_type)
        temp_thumb.seek(0)
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        super().save()

        return True



