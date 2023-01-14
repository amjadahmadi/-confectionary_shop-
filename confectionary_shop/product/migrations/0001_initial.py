# Generated by Django 4.1.3 on 2022-12-18 13:13

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('Cake_designing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('category_name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, default='draw1.png', null=True, upload_to='')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
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
                ('kilo', models.FloatField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('category', models.ManyToManyField(to='product.category')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            bases=('core.basemodel',),
            managers=[
                ('stock_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('amount', models.FloatField()),
                ('percent', models.BooleanField()),
                ('active', models.BooleanField()),
                ('cake_designing_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cake_designing.cake_designing')),
                ('product', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dis', to='product.stock')),
            ],
            bases=('core.basemodel',),
        ),
    ]
