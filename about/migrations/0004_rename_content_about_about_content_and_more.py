# Generated by Django 4.2.16 on 2024-11-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='content',
            new_name='about_content',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='profile_image',
            new_name='about_logo_image',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='title',
            new_name='about_title',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='updated_on',
            new_name='about_updated_on',
        ),
    ]
