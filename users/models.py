from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CreateUserManager(BaseUserManager):

    def create_superuser(self, email, user_name,  password,**other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.setdefault('is_staff') is not True:
            raise ValueError(_(
                'SuperUser must be assigned is_staff true'))
        return self.create_user(email,user_name,password,**other_fields)

    def create_user(self, email, user_name,  password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email"))
        # if not user_name:
        #     raise ValueError(_('You must enter a user_name'))
        other_fields.setdefault('is_active',True)
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user
class CustomUser (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=254, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects=CreateUserManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.user_name