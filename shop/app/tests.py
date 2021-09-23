from django.test import TestCase
from .models import Employee, Item, Sale
from .views import *


class TestFullCycleTest(TestCase):
    fixtures = ['initial_app_data.json']


    def test_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


    def test_view_detail(self):
        resp = self.client.get('/')
        print(str(resp.content))
        fruit_list = ['Pineapple', 'Banana', 'Grape', ]
        for fruit in fruit_list:
            if fruit in str(resp.content):
                result = True
            else:
                result = False
            self.assertEqual(result, True)

    





