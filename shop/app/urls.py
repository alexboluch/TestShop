from django.views.generic import RedirectView
from django.urls import path, include 
from .views import main_view, ItemBuyView, Registration, sales_history_view, prices_history_view

urlpatterns = [
    path('', main_view, name='main'),
    path('item/<uuid:pk>/', ItemBuyView.as_view(), name='item_detail'),
    path('registration/', Registration.as_view(), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sales/', sales_history_view),
    path('prices/', prices_history_view),
]