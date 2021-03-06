from django.test import TestCase
from .models import Category,Photo

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="Fashion")
        # self.cat.save_category()
        
        self.photo = Photo(description='image test', category=self.cat)
        self.photo.save_photo()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Photo))

    def tearDown(self):
        self.image.delete_image()
        self.cat.delete_category()
        self.loc.delete_location()

    def test_save_method(self):
        self.image.save_image()
        photos  = Photo.objects.all()
        self.assertTrue(len(photos)>0)
        
    def test_search_by_category(self):
        photos = Photo.search_by_category('fashion')
        self.assertTrue(len(photos)>0)
        
class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
