# Generated by Django 5.0.6 on 2024-07-08 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='registraion_date',
            new_name='registration_date',
        ),
    ]
