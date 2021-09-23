from django.views.generic import RedirectView
from django.urls import path, include 
from .views import main_view, item_buy_view, registration

urlpatterns = [
    path('', main_view, name='main'),
    path('item/<uuid:pk>/', item_buy_view, name='item_detail'),
    path('registration/', registration),
    path('accounts/', include('django.contrib.auth.urls')),
]