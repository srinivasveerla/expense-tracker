# Generated by Django 5.0.4 on 2024-04-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancesheet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancesheets',
            name='title',
            field=models.CharField(default="<django.db.models.query_utils.DeferredAttribute object at 0x103171d80>'s Balancesheet", max_length=30, verbose_name='Balancesheet name'),
        ),
    ]
