# Generated by Django 3.1.2 on 2020-10-05 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_auto_20201004_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='sub_topics',
            field=models.ManyToManyField(blank=True, related_name='_topic_sub_topics_+', to='base.Topic'),
        ),
    ]