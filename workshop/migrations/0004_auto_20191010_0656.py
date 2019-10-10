# Generated by Django 2.2.6 on 2019-10-10 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20191009_1206'),
        ('workshop', '0003_auto_20191010_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='council',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clubs', to='workshop.Council'),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('resources', models.TextField(blank=True, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to='workshop.Club')),
                ('contacts', models.ManyToManyField(blank=True, related_name='workshop_contact', to='authentication.UserProfile')),
            ],
        ),
    ]