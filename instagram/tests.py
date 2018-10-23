from django.test import TestCase
from .models import Image,Profile, Comment
# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.new_image = Image(image_name='dog', image_caption='few text on different details',image='media/dalma.jpg', likes='1')
        self.new_image.save_image()
        self.new_image = Image(image_name='dog', image_caption='few text on different details',image='media/dalma.jpg', likes='1')

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


class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='dk',first_name='d',last_name='k',email='dk@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_data(self):
        self.assertTrue(self.user.username,"brighton")
        self.assertTrue(self.user.first_name,"asumnai")
        self.assertTrue(self.user.last_name,'angaay')
        self.assertTrue(self.user.email,'dk@asumanibrighton@gmail.com')

    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)

class ProfileTest(TestCase):
    def setUp(self):
        self.new_user=User(username='brighton',first_name='asumani',last_name='angaya',email='asumani@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,bio='i love Dogs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_data(self):
        self.assertTrue(self.new_profile.bio,"wuehh")
        self.assertTrue(self.new_profile.user,self.new_user)

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)


    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='love dogs').update(bio = 'love dogsd')
        self.updated_profile = Profile.objects.get(bio='love dogs')
        self.assertTrue(self.updated_profile.bio,'love dogs')

class CommentTest(TestCase):
    def setUp(self):
        self.new_user=User(username='brighg',first_name='asus',last_name='anga',email='asumani@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,bio='lady exempt')
        self.new_profile.save()
        self.new_Image = Image(user=self.new_user,caption="caption",profile=self.new_profile)
        self.new_Image.save()
        self.comment=Comments(user=self.new_user,Image=self.new_Image,comment='haha')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_data(self):
        self.assertTrue(self.comment.comment,"haha")

    def test_comments(self):
        self.comment.save()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)>0)
