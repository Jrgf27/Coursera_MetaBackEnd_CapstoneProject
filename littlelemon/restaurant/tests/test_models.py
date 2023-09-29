from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):

    def test_get_menu_title(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        title = f'{item.title} : {str(item.price)}'
        self.assertEqual( str(item) , title)