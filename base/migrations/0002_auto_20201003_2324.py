# Generated by Django 3.1.2 on 2020-10-04 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name']},
        ),
    ]
