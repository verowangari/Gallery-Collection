from django.db import models

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
    


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField(max_length=500, null=False,blank=False)
    
    @classmethod
    def search_by_category(cls,category):
        photos = cls.objects.filter(category__icontains=category)
        return photos
    
    def __str__(self):
        return self.description
    
class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=False)
    
    
    def __str__(self):
        return self.name