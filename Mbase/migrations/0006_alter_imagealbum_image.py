# Generated by Django 4.0.3 on 2022-09-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mbase', '0005_alter_imagealbum_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagealbum',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]