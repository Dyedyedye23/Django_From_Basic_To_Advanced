# Generated by Django 5.1.1 on 2024-10-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_boss'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='城市名')),
                ('count', models.IntegerField(verbose_name='人口数量')),
                ('img', models.FileField(max_length=128, upload_to='city/', verbose_name='Logo')),
            ],
        ),
    ]
