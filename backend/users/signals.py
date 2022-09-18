from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from users.models import Profile

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

        subject = "Welcome to DevSearch"
        message = "We are glad you are here"
 
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=True
        )


@receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs) -> None:
    try:
        user = instance.user
        user.delete()
    except:
        pass

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