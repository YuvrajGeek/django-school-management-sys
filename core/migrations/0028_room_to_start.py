# Generated by Django 3.1.4 on 2020-12-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='to_start',
            field=models.CharField(default='Not Provided / May Start Anytime', max_length=256),
        ),
    ]
