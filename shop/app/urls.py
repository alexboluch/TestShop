from django.views.generic import RedirectView
from django.urls import path
from .views import main_view

urlpatterns = [
    path('main/', main_view, name='main'),
    path('', RedirectView.as_view(url='/main/', permanent=True))
]