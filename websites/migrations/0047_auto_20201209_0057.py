# Generated by Django 3.0.8 on 2020-12-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0046_auto_20201208_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='maximum',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='groups',
            name='minimum',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='groups',
            name='price_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Only use the product price'), (2, 'Sum all the groups price'), (3, 'Average all the groups price'), (4, 'Add the product price to the sum groups price'), (5, 'Add the product price to the average groups price')], default=1, verbose_name='How is the price calculated?'),
        ),
        migrations.AlterField(
            model_name='options',
            name='maximum',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='options',
            name='minimum',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Only use the product price'), (2, 'Sum all the groups price'), (3, 'Average all the groups price'), (4, 'Add the product price to the sum groups price'), (5, 'Add the product price to the average groups price')], default=1, verbose_name='How is the price calculated?'),
        ),
    ]
