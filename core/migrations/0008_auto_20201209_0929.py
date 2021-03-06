# Generated by Django 3.1.4 on 2020-12-09 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201208_2343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
