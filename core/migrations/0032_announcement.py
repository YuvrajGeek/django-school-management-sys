# Generated by Django 3.1.4 on 2020-12-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_homework_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
