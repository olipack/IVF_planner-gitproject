# Generated by Django 3.1.5 on 2021-01-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_auto_20210127_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='prescription',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]
