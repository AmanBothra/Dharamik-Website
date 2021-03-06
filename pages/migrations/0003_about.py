# Generated by Django 4.0.3 on 2022-03-31 14:21

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_videobanner_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=50, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(default='', verbose_name='Description')),
                ('image', models.FileField(upload_to='home/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])], verbose_name='Backgroung Image')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
    ]
