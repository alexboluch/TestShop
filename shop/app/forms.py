from django import forms
from .models import Item, Employee, Sale
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


QUANTITY_CHOICES = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
]

    

class ItemBuyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    quantity = forms.ChoiceField(initial=1, widget=forms.Select(), choices=QUANTITY_CHOICES)
    price = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = Item
        fields = '__all__'


class RegistrForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='This field is required',validators=[EmailValidator])
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

