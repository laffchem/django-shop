# Generated by Django 5.1.4 on 2024-12-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_id_alter_orderitem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
