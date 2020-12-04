# Generated by Django 2.2.10 on 2020-12-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0028_auto_20201127_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='audience',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workshopresource',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
