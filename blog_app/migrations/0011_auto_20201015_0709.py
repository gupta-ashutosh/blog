# Generated by Django 3.1 on 2020-10-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20201015_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='introduction',
            field=models.TextField(default=''),
        ),
    ]