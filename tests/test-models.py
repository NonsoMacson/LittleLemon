from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):

    def test_get_item(self):
        item= Menu.objects.create(title='Beans', price= 11.38, inventory=20)
        self.assertEqual(str(item), 'Beans : 11.38')