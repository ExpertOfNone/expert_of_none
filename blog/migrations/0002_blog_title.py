# Generated by Django 3.1.2 on 2020-10-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
