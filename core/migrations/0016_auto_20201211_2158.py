# Generated by Django 3.1.4 on 2020-12-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201211_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='std',
            field=models.IntegerField(default=1),
        ),
    ]
