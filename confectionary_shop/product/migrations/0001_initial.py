# Generated by Django 4.1.3 on 2022-12-04 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cake_designing', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('category_name', models.CharField(max_length=100)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Discount_Code',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('discount_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('percent', models.BooleanField()),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('product_name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('kilo', models.FloatField(null=True)),
                ('count', models.IntegerField(null=True)),
                ('price', models.FloatField()),
                ('after_discount', models.FloatField(null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('amount', models.FloatField()),
                ('percent', models.BooleanField()),
                ('active', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cake_designing_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Cake_designing.cake_designing')),
                ('category_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.stock')),
            ],
            bases=('core.basemodel',),
        ),
    ]