# Generated by Django 2.2.6 on 2020-03-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_userprofile_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo_url',
            field=models.URLField(blank=True, editable=False, null=True),
        ),
    ]
