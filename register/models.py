from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# telefon numarası içinde bir alan lazım buraya
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    privateKey = models.CharField(_('privateKey'), unique=True, max_length=100)
