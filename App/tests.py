from django.test import TestCase
from django.urls import reverse

from App import factories, models

class StoreTestCase(TestCase):
    def setUp(self):
        self.product = factories.ProductFactory()
        self.product2 = factories.ProductFactory()
        self.user = factories.UserFactory()
        self.user2 = factories.UserFactory()
        self.category = factories.ProductCategoryFactory()

    def test_get_product_list(self):
        print()
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('list:', 'success')
        self.assertEqual(response.context['products'].count(), models.Product.objects.count())
        print('products_list:', response.context['products'].count(), models.Product.objects.count())

    def test_users_count(self):
        print()
        self.assertEqual(models.User.objects.count(), 2)
        print('users:', models.User.objects.count())

    def test_get_product_detail(self):
        print()
        url = reverse('product_details', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('detail:', 'success')

    def test_update_product(self):
        print()
        url = reverse('product_update', kwargs={'pk': self.product.pk})
        old_name = self.product.product_name
        old_price = self.product.price
        old_description = self.product.description
        old_category = self.product.category
        response = self.client.post(url, {'product_name': 'new', 'price': 500,
                                          'description': old_description, 'category': old_category})
        self.product.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        print('update:', 'success')
        self.assertNotEqual(self.product.product_name, old_name)
        print('updated:',self.product.product_name, old_name)
        self.assertEqual(self.product.category, old_category)
        print('not updated:', self.product.category, old_category)

    def test_delete_product(self):
        print()
        url = reverse('product_delete', kwargs={'pk': self.product.pk})
        old_product_count = models.Product.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        print('delete:', 'success')
        self.assertGreater(old_product_count, models.Product.objects.count())
        print('delete:', old_product_count, models.Product.objects.count())

    def test_create_product(self):
        print()
        url = reverse('product_create')
        old_product_count = models.Product.objects.count()
        response = self.client.post(url, {'product_name': 'name', 'price': 250,
                                            'description': 'desc', 'category': self.category.id})
        self.assertEqual(response.status_code, 302)
        print('create:', 'success')
        self.assertLessEqual(old_product_count, models.Product.objects.count())
        print('crete:', old_product_count, models.Product.objects.count())

        new_product = models.Product.objects.last()
        self.assertEqual(new_product.product_name, 'name')
