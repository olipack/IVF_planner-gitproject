# Generated by Django 3.1.5 on 2021-01-24 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20210124_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cycletype',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='drugclass',
            options={},
        ),
        migrations.AlterModelOptions(
            name='prescriptiongroup',
            options={},
        ),
        migrations.RemoveField(
            model_name='drug',
            name='order',
        ),
        migrations.RemoveField(
            model_name='drugclass',
            name='order',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='order',
        ),
        migrations.RemoveField(
            model_name='prescriptiongroup',
            name='order',
        ),
    ]
