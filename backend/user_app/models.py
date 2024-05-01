from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    PROVIDERS = [
        ("G","Google"),
        ("E","Email")
    ]
    username = models.CharField(verbose_name="Username",max_length=30, unique=True, blank=False, null=False)
    provider = models.CharField(verbose_name="Provider",max_length=2,choices=PROVIDERS,default="E")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("email",)

    def __str__(self) -> str:
        return self.username