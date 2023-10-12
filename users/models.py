from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    tg_id = models.CharField(verbose_name='id telegram', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

