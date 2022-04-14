from accounts.models import User, OTPCode
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.utils import send_sms

@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        code = OTPCode.objects.create(user=instance)
        print(code.user)
        # send_sms(code.code, code.user.number)