# Generated by Django 3.2.3 on 2021-08-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
