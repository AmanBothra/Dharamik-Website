# Generated by Django 4.0.3 on 2022-04-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_subscriber_international_clients_users_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredinphoto',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
