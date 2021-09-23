from django.views.generic import RedirectView
from django.urls import path, include 
from .views import main_view, item_buy_view, registration, sales_history_view, prices_history_view

urlpatterns = [
    path('', main_view, name='main'),
    path('item/<uuid:pk>/', item_buy_view, name='item_detail'),
    path('registration/', registration),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sales/', sales_history_view),
    path('prices/', prices_history_view),
]
prices_history_view