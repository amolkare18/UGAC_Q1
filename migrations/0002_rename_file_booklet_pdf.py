# Generated by Django 5.0.6 on 2024-06-19 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKLET', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booklet',
            old_name='file',
            new_name='pdf',
        ),
    ]