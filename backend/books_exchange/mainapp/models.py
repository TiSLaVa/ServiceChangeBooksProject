from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name='имя', max_length=25, blank=False, null=False)
    last_name = models.CharField(verbose_name='фамилия', max_length=50, blank=False, null=False)
    middle_name = models.CharField(verbose_name='отчество', max_length=25, blank=False, null=False)
    email = models.EmailField(verbose_name='e-mail', max_length=35, unique=True, blank=False, null=False)
    username = models.CharField(verbose_name='имя в приложении', max_length=20, unique=True, blank=False, null=False)
    password = models.CharField(verbose_name='пароль', max_length=128, blank=False, null=False)
    rating = models.PositiveSmallIntegerField(verbose_name='рейтинг', default=0)
    date_joined = models.DateTimeField(verbose_name='дата регистрации', default=timezone.now)
