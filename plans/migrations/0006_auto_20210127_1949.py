# Generated by Django 3.1.5 on 2021-01-27 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_auto_20210127_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ['group', 'order']},
        ),
        migrations.AlterModelOptions(
            name='procedure',
            options={'ordering': ['description', 'description']},
        ),
    ]
