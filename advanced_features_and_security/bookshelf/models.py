# bookshelf/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custom manager for our CustomUser model."""

    def create_user(self, username, email, password=None, **extra_fields):
        """Create and save a regular user."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and save a superuser with admin permissions."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Our custom user model.
    We are still keeping the username field (comes from AbstractUser),
    but we are making email the unique identifier for login.
    """

    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    # Tell Django to use email as the login field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # still require username when creating superusers

    objects = CustomUserManager()

    def __str__(self):
        return self.email or self.username


class Book(models.Model):
    """Example book model."""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
