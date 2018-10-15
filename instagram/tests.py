from django.test import TestCase
from .models import Image,Profile, Comment
# Create your tests here.
class instagram_TestCases(TestCase):
    def setUp(self):
        self.new_image = Image(image_name='dog', image_caption='few text on different details',image='media/dalma.jpg')
        self.new_image.save_image()
        self.new_image = Image(image_name='dog', image_caption='few text on different details',image='media/dalma.jpg')

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
        Comment.objects.all().delete()
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        specific = Image.objects.filter(image_name='dog')
        Image.delete_image(specific)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_display_all_objects_method(self):
        self.new_image.save_image()
        images = Image.retrieve_all()
        self.assertEqual(images.image_name,'dog')


    def test_update_single_object_property(self):
        self.new_image.save_image()
        specific =Image.update_image('dog','dalma')
        fetched = Image.objects.get(image_name='dalma')
        self.assertEqual(fetched.image_name,'dalma')

    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)
