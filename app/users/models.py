from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email',unique=True)
    first_name = models.CharField(verbose_name='first_name',max_length=30,blank=True)
    last_name = models.CharField(verbose_name='last_name',max_length=30,blank=True)
    second_name = models.CharField(verbose_name='second_name',max_length=30,blank=True)
    is_active = models.BooleanField(verbose_name='is_active',default=True)
    avatar = models.ImageField(upload_to='upload_media/users/avatar/',null=True,blank=True,default='upload_media/users/avatar/shablon.jpg')
    age = models.PositiveSmallIntegerField(verbose_name='age',null=True,blank=True,default=0)
    date_joined = models.DateTimeField(verbose_name='date_joined',auto_now=True)
    date_update_info = models.DateTimeField(verbose_name='date_joined',auto_now=True)
    is_staff = models.BooleanField(verbose_name='is_staff',default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    def get_full_name(self):
        return self.first_name +' '+self.second_name +' '+self.last_name
    def get_id(self):
        return self.id
    def email_user(self,subject,message,from_email=None,**kwargs):
        send_mail(subject,message,from_email,[self.email],**kwargs)
