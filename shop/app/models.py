from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    address = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name

    @property
    def get_name(self):
        return self.name


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    seller = models.ForeignKey(Employee, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']

    def get_absolute_url(self):
        return reverse ('item_detail', args = [str(self .id)])

    def __str__(self):
        return self.title

    @property
    def get_seller_name(self):
        return str(self.seller.get_name)



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

    def __str__(self):
        return str(self.item) + ", " + str(self.quantity) + " piec., " + str(self.seller) + ", " + str(self.create_date)


class NewPrice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    new_price = models.IntegerField()
    seller = models.ForeignKey(Employee, on_delete=models.CASCADE)
    changes_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-changes_date']

    def __str__(self):
        return str(self.item) + ", to - $" + str(self.new_price) + ", " + str(self.changes_date)
