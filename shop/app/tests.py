from django.test import TestCase
from .models import Employee, Item, Sale, NewPrice
from .views import *
from django.test import Client

class TestFullCycleTest(TestCase):
    fixtures = ['initial_app_data.json', 'initial_data.json',]

#Test main page
    def test_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

#Test login and view pages for only users which already login
    def test_login_and_view(self):
        login = self.client.login(username='admin', password='admin')
        resp = self.client.get('/sales/')
        self.assertEqual(resp.status_code, 200)
        resp1 = self.client.get('/prices/')
        self.assertEqual(resp1.status_code, 200)

#Test main page and search items names
    def test_view_detail(self):
        resp = self.client.get('/')
        fruit_list = ['Pineapple', 'Banana', 'Grape', ]
        for fruit in fruit_list:
            if fruit in str(resp.content):
                result = True
            else:
                result = False
            self.assertEqual(result, True)

#Test create Employee, Item and changing items price and create obj - NewPrice
    def test_add_new_item_and_change_price(self):
        new_seller = Employee(name="Test seller")
        new_seller.save()
        title = "Test item"
        price = 50
        description = "Test description"
        new_item = Item(
            title=title,
            price=price,
            description=description,
            seller=new_seller
        )
        new_item.save()
        alterable_item = Item.objects.get(title=title)
        alterable_item.price = 100
        alterable_item.save()
        changed_item = Item.objects.get(title=title)
        self.assertEqual(changed_item.price, 100)
        new_price = NewPrice.objects.get(item=changed_item, new_price=100)
        self.assertEqual(new_price.new_price, 100)




    





