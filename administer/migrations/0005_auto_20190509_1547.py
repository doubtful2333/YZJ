# Generated by Django 2.2 on 2019-05-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administer', '0004_auto_20190509_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tally',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]
