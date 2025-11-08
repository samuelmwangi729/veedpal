from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone

class UserRoles:
    SUPER_ADMIN = "super_admin"
    USER = "user"
    MODERATOR = "moderator"
    SUPPORT = "support"

    choices = (
        (SUPER_ADMIN, "super_admin"),
        (USER, "user"),
        (MODERATOR, "moderator"),
        (SUPPORT, "support")
    )

# Custom user manager
class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The username is required")
        if not email:
            raise ValueError("The email is required")
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", UserRoles.SUPER_ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

# Custom user model
class CustomUserModel(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=False, unique=True)
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.USER)
    objects = CustomUserManager()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    # Set email as the login field
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"  # login will now use email
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]  # username required for creation

    def __str__(self):
        return self.email  # optional: shows email instead of username

    def save(self, *args, **kwargs):
        if self.is_verified and self.verified_at is None:
            self.verified_at = timezone.now()
        super().save(*args, **kwargs)
