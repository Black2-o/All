# Generated by Django 5.0.6 on 2024-06-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_bookpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
