# Generated by Django 3.1.2 on 2020-10-10 01:35

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_topic_top_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/files/photos'), upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(help_text='Required and will be used as description and alt-text for Images')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together={('name', 'parent_topic')},
        ),
    ]
