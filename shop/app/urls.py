from django.views.generic import RedirectView
from django.urls import path
from .views import main_view, item_buy_view

urlpatterns = [
    path('', main_view, name='main'),
    path('item/<uuid:pk>/', item_buy_view, name='item_detail'),
]