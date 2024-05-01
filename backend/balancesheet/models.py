from django.db import models
from user_app.models import CustomUser
# Create your models here.
class BalanceSheets(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name="user_id")
    title = models.CharField(verbose_name="Balancesheet name",max_length=30, default=f"{CustomUser.username}'s Balancesheet")

    def __str__(self):
        return self.title