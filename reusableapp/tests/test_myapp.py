from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from myapp.models import RootModel
from tests.models import Article, Author


class MyAppTestCase(APITestCase):
    def test_one(self):
        self.assertEqual(1, 1)

    def test_create_models(self):
        autor = Author.objects.create(name='Ivan')
        Article.objects.create(
            title='Title', author=autor, body='Body', category='News')
        RootModel.objects.create(some_text='Some text')

    def test_views(self):
        r = self.client.post(reverse('myapp:author-list'), data={'name': 'Bill'})
        self.assertTrue(r)
        self.assertEqual(r.status_code, 201)
