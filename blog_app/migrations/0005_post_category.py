# Generated by Django 3.1 on 2020-08-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]
