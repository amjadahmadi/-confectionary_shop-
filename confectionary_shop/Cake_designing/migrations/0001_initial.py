# Generated by Django 4.1.3 on 2022-12-18 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('feeling_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('Taste_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Cake_Designing',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('sample_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('print_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('ready_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('payment_status', models.CharField(choices=[('PR', 'Pre Payment'), ('PY', 'Payed')], default='PR', max_length=2)),
                ('extra_payment', models.FloatField(blank=True, null=True)),
                ('feeling_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cake_designing.feeling')),
            ],
            bases=('core.basemodel',),
        ),
    ]
