# Generated by Django 3.1.2 on 2020-12-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20201204_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default=None, max_length=90),
        ),
    ]
