from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item, NewPrice


@receiver(post_save, sender=Item)
def post_save_create_new_price(sender, instance, **kwargs):
    new_price = NewPrice(
        new_price=instance.price,
        item=instance,
        seller=instance.seller,
            )
    new_price.save()    

