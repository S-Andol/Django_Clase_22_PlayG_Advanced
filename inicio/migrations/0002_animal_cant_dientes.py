# Generated by Django 4.1.7 on 2023-04-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='cant_dientes',
            field=models.IntegerField(null=True),
        ),
    ]
