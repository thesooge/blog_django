from django.test import TestCase
from django.shortcuts import reverse 
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from .models import BlogPost

# Create your tests here.

class TestBlog(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.post = BlogPost.objects.create(
            title = 'hello',
            text = 'how are you',
            status = 'pub',
            author = self.user
            )
        

    
    def test_home_page_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_name(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)    

    def test_detail_page_url(self):
        response = self.client.get(reverse('post_detail', args=(self.post.id,)))
        self.assertEqual(response.status_code, 200)

    def test_delete_page_url(self):
        response = self.client.get(reverse('delete', args=(self.post.id,)))
        self.assertEqual(response.status_code, 200)

    def test_update_page_url(self):
        response = self.client.get(reverse('update_post', args=(self.post.id,)))
        self.assertEqual(response.status_code, 200)

    def test_addpost_page_url(self):
        response = self.client.get(reverse('addpost'))
        self.assertEqual(response.status_code, 200)    

    def test_post_contains(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)
        self.assertContains(response, self.post.author)

    def test_post_created(self):
        self.client.post('addpost', {'title':'hi', 'text' : 'how', 'status':'pub', 'author':self.user})
        response = self.client.get(reverse('home'))
        self.assertContains(response, self.post.title)