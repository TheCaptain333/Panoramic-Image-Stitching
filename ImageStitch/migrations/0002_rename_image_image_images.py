# Generated by Django 4.1 on 2023-07-23 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ImageStitch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='Images',
        ),
    ]