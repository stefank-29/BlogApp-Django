# Generated by Django 3.1.4 on 2020-12-20 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201219_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='account.png', upload_to='profile-pics'),
        ),
    ]