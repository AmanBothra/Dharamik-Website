# Generated by Django 4.0.3 on 2022-04-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_remove_subscriber_international_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='international_clients_users',
            field=models.IntegerField(default='', verbose_name='International Clients'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='premium_clients_users',
            field=models.IntegerField(default='', verbose_name='Premium Clients'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='subscriber_users',
            field=models.IntegerField(default='', verbose_name='Subscriber'),
        ),
    ]
