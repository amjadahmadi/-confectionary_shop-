from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, Bank_Account


@receiver(post_save, sender=User)
def create_profile(sender, instance: User, created, **kwargs):
    if created:

        user_profile = Profile.objects.create()
        instance.profile = user_profile
        instance.save()


@receiver(post_save, sender=User)
def create_bank_account(sender, instance: User, created, **kwargs):
    if created:
        user_bank_account = Bank_Account.objects.create()
        instance.bank_account = user_bank_account
        instance.save()