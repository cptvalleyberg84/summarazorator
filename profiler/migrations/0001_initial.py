# Generated by Django 4.2.16 on 2024-11-06 14:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_post_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('last_comments', models.ManyToManyField(blank=True, limit_choices_to=6, related_name='profile_comments', to='forum.comment')),
                ('last_posts', models.ManyToManyField(blank=True, limit_choices_to=3, related_name='profile_posts', to='forum.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiler', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
