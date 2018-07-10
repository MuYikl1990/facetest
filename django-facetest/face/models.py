from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Image(Name):
    img = models.ImageField(upload_to='picture')

class Number(models.Model):
    pic = models.ForeignKey(Image, on_delete=models.CASCADE)
    people_number = models.IntegerField()

    def __str__(self):
        return self.people_number
