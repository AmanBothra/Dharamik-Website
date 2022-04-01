# Generated by Django 4.0.3 on 2022-04-01 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='FaqModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(default='', max_length=255, verbose_name='Question')),
                ('answer', models.TextField(default='', max_length=10000, verbose_name='Answer')),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='about.faq')),
            ],
            options={
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]