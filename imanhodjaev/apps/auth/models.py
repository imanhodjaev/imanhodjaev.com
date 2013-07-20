from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    def full_name(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username

    USERNAME_FIELD = 'email'
