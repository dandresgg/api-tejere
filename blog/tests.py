from django.test import TestCase
from rest_framework.test import APIRequestFactory
from blog.models import Post

from blog.views import PostViewSet


class BlogTest(TestCase):
    ''' Blog test methods '''

    def setUp(self) -> None:
        self.post = Post.objects.create(title='title',
                                        description='description',
                                        body='body')

    def test_post_view_set(self) -> None:
        ''' Post view test '''
        print("post_viewset_test")
        factory = APIRequestFactory()
        view = PostViewSet.as_view(actions={'get': 'retrieve'})
        request = factory.get('post', args=(self.post.pk,))
        response = view(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 200)

    def test_post_model_title(self) -> None:
        ''' Post model title test '''
        print("post_title_test")
        field_label = self.post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_post_model_description(self) -> None:
        ''' Post model description test '''
        print("post_description_test")
        field_label = self.post._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_post_model_img(self) -> None:
        ''' Post model image test '''
        print("post_img_test")
        field_label = self.post._meta.get_field('img').verbose_name
        self.assertEqual(field_label, 'img')

    def test_post_model_created(self) -> None:
        ''' Post model created test '''
        print("post_created_test")
        field_label = self.post._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')

    def test_post_model_modified(self) -> None:
        ''' Post model modified test '''
        print("post_modified_test")
        field_label = self.post._meta.get_field('modified').verbose_name
        self.assertEqual(field_label, 'modified')
