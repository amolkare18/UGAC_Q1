# Generated by Django 5.0.6 on 2024-06-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKLET',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='BOOKLETS/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]