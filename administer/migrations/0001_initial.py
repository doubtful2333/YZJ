# Generated by Django 2.2 on 2019-05-09 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('g_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Replenish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ShopStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.IntegerField()),
                ('goods_id', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_type', models.IntegerField(max_length=32)),
                ('amount', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('u_type', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=64, null=True)),
                ('tel', models.CharField(max_length=32, null=True)),
                ('email', models.EmailField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('status', models.CharField(max_length=32)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administer.Goods')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administer.User')),
            ],
        ),
        migrations.CreateModel(
            name='ShopOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=32)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administer.Goods')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administer.Shop')),
            ],
        ),
    ]
