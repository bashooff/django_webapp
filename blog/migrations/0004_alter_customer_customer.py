# Generated by Django 3.2.3 on 2021-05-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
