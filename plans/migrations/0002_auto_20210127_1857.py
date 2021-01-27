# Generated by Django 3.1.5 on 2021-01-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0002_auto_20210126_2316'),
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='drug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='drug', to='drugs.drug', verbose_name='Drug'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='drug1', to='drugs.drug', verbose_name='Drug 1'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='drug2', to='drugs.drug', verbose_name='Drug 2'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='drug3', to='drugs.drug', verbose_name='Drug 3'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='drug4', to='drugs.drug', verbose_name='Drug 4'),
        ),
    ]