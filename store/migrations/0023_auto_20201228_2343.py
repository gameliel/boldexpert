# Generated by Django 3.1.2 on 2020-12-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20201228_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='product', to='store.Tag'),
        ),
    ]