# Generated by Django 4.2.4 on 2023-08-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventplatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signins', models.BooleanField()),
                ('username', models.CharField(max_length=255)),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]