# Generated by Django 3.1.4 on 2020-12-10 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201209_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(default='Not Provided'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default='Not Provided', max_length=20),
        ),
    ]
