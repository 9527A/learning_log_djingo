# Generated by Django 2.0 on 2019-03-24 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_apped',
            new_name='date_added',
        ),
    ]
