# Generated by Django 4.0.6 on 2022-07-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0004_alter_pricedata_date_alter_pricedata_marketcap_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='marketcap',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='pricedata',
            name='price',
            field=models.BigIntegerField(),
        ),
    ]