from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance: User, created: bool, **kwargs) -> None:
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email
        )

@receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs) -> None:
    user = instance.user
    user.delete()

@receiver(post_save, sender=Profile)
def update_profile(sender: Profile, instance: Profile, created: bool, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

# -- Without decorator
# post_save.connect(create_profile, sender=User)
# post_delete.connect(profile_deleted, sender=Profile)