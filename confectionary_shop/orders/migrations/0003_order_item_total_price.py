# Generated by Django 4.1.3 on 2022-12-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_item_discription_order_item_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='total_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]