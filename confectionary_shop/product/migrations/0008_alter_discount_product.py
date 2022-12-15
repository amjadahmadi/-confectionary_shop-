# Generated by Django 4.1.3 on 2022-12-14 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_discount_cake_designing_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='product.stock'),
        ),
    ]