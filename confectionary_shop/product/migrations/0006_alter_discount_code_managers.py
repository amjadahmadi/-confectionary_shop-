# Generated by Django 4.1.3 on 2023-01-01 16:03

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_discount_code_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='discount_code',
            managers=[
                ('active_manger', django.db.models.manager.Manager()),
            ],
        ),
    ]