"""Make thumbs for images."""

from django.db.models.fields.files import ImageFiled, ImageFieldFile
from PIL import Image
import os

def _add_thumb(s):
    """Change string(filename, URL) with filename of image, and insert
    '.thumb' before '.jpg').
    """
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)

class ThumbnailImageField(ImageField):
    """
    Save miniature (JPEG) pictures and open methods:
    get_FIELD_thumb_url() and get_FIELD_thum_filename().
    
    get two args: thumb_width and thumb_height, with default value 128
    pixels.
    """
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)


class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)
        img.thumbnail(
                (self.field.thumb_width, self.field.thumb_height),
                Image.ANTIALIAS
        )
        img.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImagesFieldFile, self).delete(save)

# How to use:
# Into models.py:
# from gallery.items.fields import ThumbnailImageField
# And change models.ImageField to image = ThumbnailImageField(upload_to='photos')
