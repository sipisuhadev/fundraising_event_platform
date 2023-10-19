# Generated by Django 4.2.4 on 2023-08-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventplatform', '0003_funds'),
    ]

    operations = [
        migrations.CreateModel(
            name='fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('goal', models.IntegerField()),
                ('message', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='funds',
        ),
    ]