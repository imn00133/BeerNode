from django.db.models.fields.files import ImageFieldFile
from django.forms import ImageField

DEFAULT_IMAGE_PATH = 'image/no_img.png'


class DefaultStaticImageFieldFile(ImageFieldFile):
    @property
    def url(self):
        try:
            return super().url
        except ValueError:
            return DEFAULT_IMAGE_PATH


class DefaultStaticImageField(ImageField):
    attr_class = DefaultStaticImageFieldFile

    def __init__(self, *args, **kwargs):
        self.static_image_path = kwargs.pop(
            'default_image_path',
            getattr(DEFAULT_IMAGE_PATH)
        )
        super().__init__(*args, **kwargs)
