# Generated by Django 3.1.7 on 2021-06-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
