from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff,
                is_superuser, *args, **kargs):
        if not email:
            raise ValueError("El email es obligario")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True,
                    is_staff=is_staff, is_superuser=is_superuser, *args, **kargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, username, email, password=None, *args, **kargs):
        return self._create_user(username, email, password, False, False, *args,
                **kargs)

    def create_superuser(self, username, email, password, *args, **kargs):
        return self._create_user(username, email, password, True, True, *args,
            **kargs)

    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.URLField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email',]

    def get_short_name(self):
        return self.username
