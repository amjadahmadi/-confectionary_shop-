# Generated by Django 4.1.3 on 2022-12-17 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
