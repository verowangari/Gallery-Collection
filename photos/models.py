from re import T
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
        
class Category (models.Model):
    name=models.CharField(max_length=100, null=False,blank=False)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=False)
    
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    # image=models.ImageField(null=False,blank=False)
    image = CloudinaryField('image')
    description=models.TextField(max_length=500, null=False,blank=False)
    location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True,blank=True)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()
    
    @classmethod
    def search_by_category(cls,category):
        photos = cls.objects.filter(category__icontains=category)
        return photos
    
    def __str__(self):
        return self.description
    
