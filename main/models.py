from django.db import models


class Ism(models.Model):
    ism = models.CharField(max_length=45)
    familiya = models.CharField(max_length=45)
    ty = models.IntegerField()


class Category(models.Model):
    translate_attributes = ["name"]
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'





def post_upload_to(instance, filename):
    return Ism('posts')(instance, filename)

def carousel_upload_to(instance, filename):
    return Ism('carousel')(instance, filename)


    
class Carousel(models.Model):
    image = models.ImageField(upload_to=carousel_upload_to)
    header = models.CharField(max_length=50, default=None, null=True)
    comment = models.CharField(max_length=150, default=None, null=True)
    