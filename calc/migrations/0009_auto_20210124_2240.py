# Generated by Django 3.1.5 on 2021-01-24 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_auto_20210124_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeingredient',
            name='drug_class',
        ),
        migrations.AddField(
            model_name='drug',
            name='drug_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='drug_class', to='calc.drugclass'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='drug1', to='calc.drug'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='drug2', to='calc.drug'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='drug3', to='calc.drug'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='drug4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='drug4', to='calc.drug'),
        ),
    ]
