# Generated by Django 3.2.3 on 2021-05-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='amount',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='orderedItemID',
            field=models.IntegerField(default=''),
        ),
    ]
