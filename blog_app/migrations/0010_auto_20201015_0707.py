# Generated by Django 3.1 on 2020-10-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_post_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='introduction',
            field=models.CharField(max_length=255),
        ),
    ]
