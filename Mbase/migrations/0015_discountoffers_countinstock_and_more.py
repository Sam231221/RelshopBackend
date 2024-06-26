# Generated by Django 4.0.3 on 2024-06-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mbase', '0014_alter_discountoffers_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountoffers',
            name='countInStock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='discountoffers',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discountoffers',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discountoffers',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='discountoffers',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='discountoffers',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
