# Generated by Django 5.1.4 on 2025-01-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('msg', models.CharField(max_length=255, verbose_name='message')),
                ('img', models.ImageField(upload_to='posts')),
            ],
        ),
    ]
