# Generated by Django 4.2.5 on 2023-09-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test_app', '0002_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='accesses',
        ),
        migrations.AddField(
            model_name='user',
            name='accesses',
            field=models.ManyToManyField(blank=True, related_name='access', to='my_test_app.product'),
        ),
    ]
