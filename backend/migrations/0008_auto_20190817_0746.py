# Generated by Django 2.2.4 on 2019-08-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190816_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='browser_version',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='currency',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='latitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='os',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='os_version',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='platform_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='platform_vendor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
