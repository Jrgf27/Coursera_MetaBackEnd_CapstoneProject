from django.test import TestCase
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="Brownie", price=23, inventory=215)
        item3 = Menu.objects.create(title="Something", price=54, inventory=321)

    def test_getall(self):

        menu_objects = Menu.objects.all()
        
        serialized_menu = MenuSerializer(menu_objects, many=True)
        for index, item in enumerate(serialized_menu.data):
            self.assertEqual(str(item['title']), str(menu_objects[index].title))
            self.assertEqual(str(item['price']), str(menu_objects[index].price))
            self.assertEqual(str(item['inventory']), str(menu_objects[index].inventory))

        # for index, serialized_item in enumerate(serialized_data):
        #     menu_item = menu_objects[index]
        #     self.assertEqual(serialized_item['title'], menu_item.title)
        #     self.assertEqual(serialized_item['price'], menu_item.price)
        #     self.assertEqual(serialized_item['inventory'], menu_item.inventory)