# Generated by Django 3.2.3 on 2021-05-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210526_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='orderedItemID',
            field=models.IntegerField(),
        ),
    ]