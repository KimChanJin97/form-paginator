# Generated by Django 4.0.4 on 2022-05-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
