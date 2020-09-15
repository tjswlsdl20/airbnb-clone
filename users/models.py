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

    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True,)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    langauge = models.CharField(max_length=2, choices=LANGAUGE_CHOICES, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)
    superhost = models.BooleanField(default=False)
