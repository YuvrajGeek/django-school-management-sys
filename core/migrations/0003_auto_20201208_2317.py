# Generated by Django 3.1.4 on 2020-12-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201208_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=256, unique=True),
        ),
    ]
