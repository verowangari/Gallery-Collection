from django.contrib import admin

# Register your models here.
from .models import Photo,Category

admin.site.Register(Category)
admin.site.Register(Photo)