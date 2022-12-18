# Generated by Django 4.1.3 on 2022-12-18 13:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^(\\+98|0)\\d{10}')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('balance', models.FloatField(default=0)),
                ('card_bank', models.CharField(max_length=100, null=True)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('gender', models.CharField(choices=[('MA', 'Male'), ('FE', 'Female')], default='MA', max_length=2)),
                ('birth_day', models.DateTimeField(null=True)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Rejected')], default=1)),
                ('object_id', models.PositiveIntegerField()),
                ('comment_body', models.TextField()),
                ('rate', models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Good'), (4, 'Very good'), (5, 'Excellent')], default=3)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('full_address', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.bank_account'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.profile'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
