# Generated by Django 4.0.3 on 2022-04-01 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_remove_featuredin_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='international_clients',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='premium_clients',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='subscriber',
        ),
    ]