# from django.dispatch import receiver
# from django.db.models.signals import pre_save, post_save
# from loguru import logger
# from django.contrib.auth import get_user_model
# from .models import *
# from stores.models import Stores
#
#
# @receiver(pre_save, sender=Stores)
# def create_store(sender, instance, **kwargs):
#     new_store = Stores(
#         img=instance.img,
#         name=instance.name,
#         description=instance.description,
#         deposit=instance.deposit,
#         rating=instance.rating,
#         category=instance.category,
#         sold=instance.sold,
#         telegram_bot=instance.telegram_bot,
#         store_type=instance.store_type,
#         rules=instance.rules,
#         works=instance.work,
#         forum=instance.forum,
#         sales=instance.sales,
#
#         cover=instance.cover
#     )
#     new_store.save()
#
#
#
#
# @receiver(pre_save, sender=NewStores)
# def create_store(sender, instance, **kwargs):
#     new_store = Stores(
#         img=instance.img,
#         name=instance.name,
#         description=instance.description,
#         deposit=instance.deposit,
#         rating=instance.rating,
#         category=instance.category,
#         sold=instance.sold,
#         telegram_bot=instance.telegram_bot,
#         rules=instance.rules,
#         works=instance.work,
#         cover=instance.cover
#     )
#     new_store.save()
