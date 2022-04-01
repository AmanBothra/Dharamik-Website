# Generated by Django 4.0.3 on 2022-04-01 12:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_keypoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(default='', max_length=50, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Fetured In',
            },
        ),
        migrations.AlterField(
            model_name='keypoints',
            name='membership_perks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='pages.membershipperks'),
        ),
        migrations.AlterField(
            model_name='profitscreenshots',
            name='image',
            field=models.FileField(upload_to='home/membership_perks/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])], verbose_name='Upload Profit Screenshot'),
        ),
        migrations.AlterField(
            model_name='profitscreenshots',
            name='membership_perks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshot', to='pages.membershipperks'),
        ),
        migrations.CreateModel(
            name='FeaturedInPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='home/featured_in/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])], verbose_name='Image')),
                ('featured_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured', to='pages.featuredin')),
            ],
            options={
                'verbose_name_plural': 'Profit Screenshots',
            },
        ),
    ]