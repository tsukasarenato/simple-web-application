# Generated by Django 3.0.7 on 2020-07-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0029_auto_20200704_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='user_input',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
