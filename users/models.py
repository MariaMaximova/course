from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


"""from datetime import timedelta
from hashlib import md5
import base64
import random
import string

from django.contrib.auth.models import AbstractUser
from django.core.signing import TimestampSigner
from django.db import models
from django.conf import settings


APHABET = (string.printable + string.ascii_letters * 3)


class User(AbstractUser):
    signer = TimestampSigner(salt='Hello World!')

    is_email_verified = models.BooleanField(default=False)
    initial_secret_key = models.CharField(null=True, max_length=256)
    verification_email_sent_at = models.DateTimeField(null=True)

    is_student = models.BooleanField(default=False)
    grade = models.PositiveSmallIntegerField(null=True)
    subgrade = models.CharField(max_length=1)

    def get_initial_key(self):
        initial_key = "".join(random.sample(APHABET, 256))
        self.initial_secret_key = initial_key
        self.save()
        return initial_key

    def get_signed_key(self):
        initial_key = self.initial_secret_key
        hashed_key = md5(bytes(initial_key, encoding='ascii')).hexdigest()
        signed_key = self.signer.sign(hashed_key)
        encoded_key = base64.b64encode(signed_key)
        return encoded_key

    def get_verification_link(self):
        self.get_initial_key()
        host = settings.HOST_NAME
        key = self.get_signed_key()
        link = f"{host}/verify-email?key={key}"
        return link

    def check_key(self, secret_key):
        decoded_key = base64.b64decode(secret_key)
        unsigned_key = self.signer.unsign(
            decoded_key,
            max_age=timedelta(days=1)
        )
        initial_key = self.initial_secret_key
        hashed_key = md5(bytes(initial_key, encoding='ascii')).hexdigest()
        return unsigned_key == hashed_key"""

