# Generated by Django 3.1.2 on 2020-10-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201003_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='sub_topics',
            field=models.ManyToManyField(related_name='_topic_sub_topic_+', to='base.Topic'),
        ),
    ]
