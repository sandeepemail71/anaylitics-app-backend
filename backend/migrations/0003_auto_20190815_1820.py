# Generated by Django 2.2.4 on 2019-08-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190815_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]