from django.test import TestCase
import datetime as dt
from django.contrib.auth.models import User
from .models import Article

# Create your tests here.

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.stephen= User(first_name = 'stephen', last_name ='ndele', password = 'test1234', email ='stephen@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.stephen,User))


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new user and saving it
        self.stephen= User(first_name = 'stephen', last_name ='ndele', email ='stephen@gmail.com')
        self.stephen.save_User()

        

        self.new_article= Article(title = 'Test Article',body = 'This is a random test Post',user = self.stephen)
        self.new_article.save()


    def tearDown(self):
        User.objects.all().delete()
        Article.objects.all().delete()

   