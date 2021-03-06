# Generated by Django 2.2.10 on 2020-11-20 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0022_auto_20201120_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopresource',
            name='event',
        ),
        migrations.AlterField(
            model_name='workshopresource',
            name='workshop',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='workshop.Workshop'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
