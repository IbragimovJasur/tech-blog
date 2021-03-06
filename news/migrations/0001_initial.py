# Generated by Django 3.2.3 on 2021-08-14 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date_of_publication', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('AI', 'Artificial Intelligence'), ('Space', 'Space related'), ('Robotics', 'Robotics'), ('General', 'General')], default='General', max_length=50)),
                ('image1', models.ImageField(upload_to='post_photo/')),
                ('slug', models.SlugField(unique=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
