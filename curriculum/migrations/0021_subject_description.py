# Generated by Django 3.1.1 on 2020-10-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0020_auto_20201003_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
