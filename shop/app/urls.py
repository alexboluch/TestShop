from django.views.generic import RedirectView
from django.urls import path

urlpatterns = [
    path('main/', main_view, name='main'),
    path('', RedirectView.as_view(url='/main/', permanent=True))
]