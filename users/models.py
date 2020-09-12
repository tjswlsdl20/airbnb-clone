from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    GENDER_FEMALE = "Female"
    GENDER_MALE = "Male"
    GENDER_OTHER = "Other"
    GENDER_CHOICES = (
        (GENDER_FEMALE, "Female"),
        (GENDER_MALE, "Male"),
        (GENDER_OTHER, "Other"),
    )

    LANGAUGE_EN = "EN"
    LANGAUGE_JP = "JP"
    LANGAUGE_CHOICES = (
        (LANGAUGE_EN, "EN"),
        (LANGAUGE_JP, "JP"),
    )

    CURRENCY_US = "USD"
    CURRENCY_JP = "JPY"
    CURRENCY_CHOICES = (
        (CURRENCY_US, "USD"),
        (CURRENCY_JP, "JPY"),
    )

    """ custom user model """

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, null=True, choices=GENDER_CHOICES, blank=True,
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    langauge = models.CharField(
        max_length=2, null=True, choices=LANGAUGE_CHOICES, blank=True
    )
    currency = models.CharField(
        max_length=3, null=True, choices=CURRENCY_CHOICES, blank=True
    )
    superhost = models.BooleanField(default=False)
