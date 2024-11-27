from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment
from django.utils.text import slugify

class ForumCRUDTest(TestCase):
    def setUp(self):
        """Set up test data."""
        # Create test users
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='testuser1',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )
        
        # Create a test post
        self.post = Post.objects.create(
            post_title='Test Post',
            post_slug=slugify('Test Post'),
            post_author=self.user1,
            post_content='Test content',
            post_status=1
        )
        
        # Create a test comment
        self.comment = Comment.objects.create(
            parent_post=self.post,
            comment_author=self.user1,
            comment_body='Test comment',
            comment_type='positive',
            comment_approved=True
        )

    def test_user_crud(self):
        """Test User CRUD operations."""
        # Test user creation
        new_user = User.objects.create_user(
            username='newuser',
            password='newpass123'
        )
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
        # Test user update
        new_user.email = 'test@example.com'
        new_user.save()
        updated_user = User.objects.get(username='newuser')
        self.assertEqual(updated_user.email, 'test@example.com')
        
        # Test user delete
        new_user.delete()
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_post_crud(self):
        """Test Post CRUD operations."""
        self.client.login(username='testuser1', password='testpass123')
        
        # Test post creation
        self.client.login(username='testuser1', password='testpass123')  # Login before creating post
        response = self.client.post(reverse('create_post'), {
            'post_title': 'New Test Post',
            'post_content': 'New test content that is at least twenty characters long',
            'post_excerpt': 'A brief summary of the test post',
            'post_status': 1
        })
        self.assertTrue(Post.objects.filter(post_title='New Test Post').exists())
        
        # Test post read
        post = Post.objects.get(post_title='New Test Post')
        response = self.client.get(reverse('post_detail', args=[post.post_slug]))
        self.assertEqual(response.status_code, 200)
        
        # Test post update
        response = self.client.post(
            reverse('post_edit', args=[post.post_slug]),
            {
                'post_title': 'Updated Test Post',
                'post_content': 'Updated content that is at least twenty characters long for validation',
                'post_excerpt': 'An updated brief summary of the test post',
                'post_status': 1
            }
        )
        updated_post = Post.objects.get(pk=post.pk)
        self.assertEqual(updated_post.post_title, 'Updated Test Post')
        
        # Test post delete
        self.client.login(username='testuser1', password='testpass123')  # Ensure user is logged in
        post = Post.objects.get(post_title='Updated Test Post')
        response = self.client.post(reverse('post_delete', args=[post.post_slug]))
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())

    def test_comment_crud(self):
        """Test Comment CRUD operations."""
        self.client.login(username='testuser1', password='testpass123')
        
        # Test comment creation
        response = self.client.post(
            reverse('post_detail', args=[self.post.post_slug]),
            {
                'comment_body': 'New test comment',
                'comment_type': 'positive'
            }
        )
        self.assertTrue(Comment.objects.filter(comment_body='New test comment').exists())
        
        # Test comment read
        comment = Comment.objects.get(comment_body='New test comment')
        response = self.client.get(reverse('post_detail', args=[self.post.post_slug]))
        self.assertEqual(response.status_code, 200)
        
        # Test comment update
        response = self.client.post(
            reverse('comment_edit', args=[self.post.post_slug, comment.pk]),
            {
                'comment_body': 'Updated test comment',
                'comment_type': 'negative'
            }
        )
        updated_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(updated_comment.comment_body, 'Updated test comment')
        
        # Test comment delete
        response = self.client.get(
            reverse('comment_delete', args=[self.post.post_slug, comment.pk])
        )
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())

    def test_authorization(self):
        """Test authorization rules."""
        # Login as user2 (not the author of the test post)
        self.client.login(username='testuser2', password='testpass123')
        
        # Try to edit post as non-author
        response = self.client.post(
            reverse('post_edit', args=[self.post.post_slug]),
            {
                'post_title': 'Unauthorized Edit',
                'post_content': 'This should not work',
                'post_status': 1
            }
        )
        post = Post.objects.get(pk=self.post.pk)
        self.assertNotEqual(post.post_title, 'Unauthorized Edit')
        
        # Try to delete post as non-author
        response = self.client.get(reverse('post_delete', args=[self.post.post_slug]))
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())
        
        # Try to edit comment as non-author
        response = self.client.post(
            reverse('comment_edit', args=[self.post.post_slug, self.comment.pk]),
            {
                'comment_body': 'Unauthorized comment edit',
                'comment_type': 'negative'
            }
        )
        comment = Comment.objects.get(pk=self.comment.pk)
        self.assertNotEqual(comment.comment_body, 'Unauthorized comment edit')
        
        # Try to delete comment as non-author
        response = self.client.get(
            reverse('comment_delete', args=[self.post.post_slug, self.comment.pk])
        )
        self.assertTrue(Comment.objects.filter(pk=self.comment.pk).exists())
