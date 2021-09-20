from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    seller = models.ForeignKey(Employee, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    final_price = models.IntegerField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Employee, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']
