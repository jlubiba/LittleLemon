from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuItemsTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=30, inventory=50)
        itm = item.get_item()
        
        self.assertEqual(itm, "IceCream : 30")