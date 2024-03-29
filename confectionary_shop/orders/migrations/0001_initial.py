# Generated by Django 4.1.3 on 2022-12-18 13:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('final_price', models.FloatField()),
                ('address', models.TextField()),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator('^(\\+98|0)\\d{10}')])),
                ('payment_status', models.CharField(choices=[('PR', 'Pre Payment'), ('PY', 'Payed')], default='PR', max_length=2)),
                ('discount_code_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.discount_code')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('amount', models.FloatField()),
                ('kilo', models.BooleanField()),
                ('price', models.FloatField()),
                ('after_discount', models.FloatField()),
                ('discription', models.TextField(blank=True, null=True)),
                ('pre_order', models.BooleanField()),
                ('ready_time', models.DateTimeField(blank=True, null=True)),
                ('discount_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.discount')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.stock')),
            ],
            bases=('core.basemodel',),
        ),
    ]
