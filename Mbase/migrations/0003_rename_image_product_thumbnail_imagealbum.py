# Generated by Django 4.0.3 on 2022-09-21 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mbase', '0002_product_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(null=True)),
                ('product', models.ForeignKey(help_text='Provide a url of image', null=True, on_delete=django.db.models.deletion.CASCADE, to='Mbase.product', verbose_name='images')),
            ],
        ),
    ]
