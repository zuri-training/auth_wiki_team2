from django.db.models.signals import post_save
from accounts.models import MyUser
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(sender, instance,created, **kwargs):
    instance.userprofile.save()
