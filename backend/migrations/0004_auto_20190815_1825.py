# Generated by Django 2.2.4 on 2019-08-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190815_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]