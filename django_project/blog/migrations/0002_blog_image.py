# Generated by Django 3.1.4 on 2020-12-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='logo.png', upload_to='blog-images'),
        ),
    ]
