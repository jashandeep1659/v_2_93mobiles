# Generated by Django 3.2.4 on 2021-06-28 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['-created_at']},
        ),
    ]
