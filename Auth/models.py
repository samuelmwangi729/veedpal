from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils import timezone

class UserRoles:
    SUPER_ADMIN="super_admin"
    USER="user"
    MODERATOR="moderator"
    SUPPORT="support"

    choices=(
        (SUPER_ADMIN,"super_admin"),
        (USER,"user"),
        (MODERATOR,"moderator"),
        (SUPPORT,"support")
        )

#create a custom user manager here that extends the base user manager

class CustomUserManager(UserManager):
    #handle the creation of a super user
    #set the roles as super admin
    def create_user(self, username, email, password=None, **extra_fields):
        #check if the username exists
        if not username:
            raise ValueError("the username is required")
        #check also if the email exists
        if not email:
            raise ValueError("the email is required")
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)
    #handles the creation of the super user
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", UserRoles.SUPER_ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
class CustomUserModel(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(blank=False,unique=True)
    role = models.CharField(max_length=20,choices=UserRoles.choices,default=UserRoles.USER)
    objects = CustomUserManager()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    #edit the field used to login the app
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name","last_name","email"]


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # if is_verified just changed to True and verified_at is empty, set timestamp
        if self.is_verified and self.verified_at is None:
            self.verified_at = timezone.now()
        super().save(*args, **kwargs)