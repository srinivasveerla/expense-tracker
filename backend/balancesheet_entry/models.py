from django.db import models
from balancesheet.models import BalanceSheets
# Create your models here.
class Entry(models.Model):
    ENTRY_TYPE = [
        ("C","Credited"),
        ("D","Debited")
    ]
    # category should include both expense and income categories
    CATEGORY = [
        ("ENT","Entertainment"),
        ("GRO","Groceries"),
        ("TRA","Transport"),
        ("FO","Food"),
    ]
    sheet_id = models.ForeignKey(BalanceSheets,on_delete=models.CASCADE,verbose_name="sheet_id")
    amount = models.DecimalField(verbose_name="amount",max_digits=10,decimal_places=4)
    created_at = models.DateTimeField(verbose_name="created at",auto_now_add=True)
    entry_type = models.CharField(max_length=3,choices=ENTRY_TYPE,default="D")
    category = models.CharField(max_length=3,choices=CATEGORY,default="FO")