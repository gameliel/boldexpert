# Generated by Django 3.1.2 on 2021-01-06 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_categorybanner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='title',
            new_name='topic',
        ),
    ]
