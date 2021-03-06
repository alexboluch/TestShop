from django import forms
from .models import Item, Employee, Sale, NewPrice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

#Best choices
QUANTITY_CHOICES = [(i, i) for i in range(1, 21)]


class ItemBuyForm(forms.ModelForm):

    quantity = forms.ChoiceField(initial=1, widget=forms.Select(), choices=QUANTITY_CHOICES)
    seller = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.item = kwargs.pop('item')
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super().save(commit=False)
        instance.item = self.item
        instance.buyer = self.user
        instance.final_price = self.item.price * instance.quantity
        instance.save()
        return instance

    class Meta:
        model = Sale
        fields = ('seller', 'quantity',)


class RegistrForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='This field is required',validators=[EmailValidator])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

