# Generated by Django 3.1.5 on 2021-01-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210124_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Price'),
        ),
    ]
