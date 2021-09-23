from django.contrib import admin
from .views import Sale, Item, Employee, NewPrice

admin.site.register(Employee)
admin.site.register(Item)
admin.site.register(Sale)
admin.site.register(NewPrice)
