from django.db import models
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)

    def _save(self, name, content):
        import os
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)
        fn = 'pic'
        name = os.path.join(d, fn+ext)

        return super(ImageStorage, self)._save(name, content)

class Image(Name):
    img = models.ImageField(upload_to='image', storage=ImageStorage())

class Number(models.Model):
    pic = models.ForeignKey(Image, on_delete=models.CASCADE)
    people_number = models.IntegerField()

    def __str__(self):
        return self.people_number
