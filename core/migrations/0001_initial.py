# Generated by Django 4.0 on 2022-03-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
