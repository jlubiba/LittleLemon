from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuItemsTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=30, inventory=50)
        itm = item.get_item()
        
        self.assertEqual(itm, "IceCream : 30")

# class MenuTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.menu = Menu.objects.create(title="IceCream", price=30, inventory=50)
        
#     def test_menu_output(self):
#         self.assertEqual(self.menu, "IceCream : 30")