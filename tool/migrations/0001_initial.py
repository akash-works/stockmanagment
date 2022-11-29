# Generated by Django 4.0.6 on 2022-07-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Company Code')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created Date and Time')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Name of Product')),
                ('serial_no', models.PositiveIntegerField(blank=True, null=True, verbose_name='Product Code')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Quantitty')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Product Added On')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.company', verbose_name='Company Name')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='image')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Image Added On')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.product')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]