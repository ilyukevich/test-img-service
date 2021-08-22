from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ..accountapp.constants import ROLE


class User(AbstractUser):
    """Model for User"""

    ROLE_USER = tuple(ROLE.items())
    role = models.CharField(
        max_length=30, choices=ROLE_USER,
        verbose_name=_('User role'),
        help_text=_('User\'s role defines all allowed actions and permissions of the user in system.')
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        help_text=_('Email is needed for password recovery, etc.'),
        unique=True,
    )

    class Meta:
        """Metadata for user model"""

        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ['date_joined']
