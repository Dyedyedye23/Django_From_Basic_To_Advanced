# Generated by Django 5.1.1 on 2024-10-01 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='depart_id',
            new_name='depart',
        ),
    ]
