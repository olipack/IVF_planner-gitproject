# Generated by Django 3.1.5 on 2021-01-24 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_auto_20210124_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='country',
            new_name='countries',
        ),
    ]