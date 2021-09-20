from django.test import TestCase
from .models import Employee, Item, Sale
from .views import *


class TestFullCycleTest(TestCase):


    def test_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


