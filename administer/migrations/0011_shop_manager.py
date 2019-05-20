# Generated by Django 2.2 on 2019-05-13 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administer', '0010_auto_20190510_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='administer.User'),
            preserve_default=False,
        ),
    ]
