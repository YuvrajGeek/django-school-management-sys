# Generated by Django 3.1.4 on 2020-12-09 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_person_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
