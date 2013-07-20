from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves a User with the given email and password. """
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = CustomUserManager.normalize_email(email)

        user = self.model(**extra_fields)

        user.email = email
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.last_login = now
        user.date_joined = now

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)

        return u


class User(AbstractBaseUser, PermissionsMixin):
    STAFF_TEXT = _('Designates whether the user can log into this admin site.')
    ACTIVE_TEXT = _('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=STAFF_TEXT)
    is_active = models.BooleanField(_('active'), default=True, help_text=ACTIVE_TEXT)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def full_name(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
