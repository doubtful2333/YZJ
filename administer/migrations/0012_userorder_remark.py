# Generated by Django 2.2 on 2019-05-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administer', '0011_shop_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='remark',
            field=models.CharField(default='无', max_length=32),
        ),
    ]
