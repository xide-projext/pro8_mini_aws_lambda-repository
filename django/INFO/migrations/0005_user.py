# Generated by Django 4.2.7 on 2023-11-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INFO', '0004_alter_yourmodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nickname', models.CharField(max_length=50)),
                # ('ID', models.EmailField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
            ],
        ),
    ]
