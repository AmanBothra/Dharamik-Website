# Generated by Django 4.0.3 on 2022-04-01 13:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_certificate_alter_membershipperks_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_name', models.CharField(default='', max_length=100, verbose_name='Book Name')),
                ('url', models.CharField(default='', max_length=255, verbose_name='Book URL')),
            ],
            options={
                'verbose_name_plural': 'Book',
            },
        ),
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='home/books/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])], verbose_name='Book Image')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='pages.recommendedbooks')),
            ],
            options={
                'verbose_name_plural': 'Book Image',
            },
        ),
    ]