# Generated by Django 3.1.1 on 2020-09-28 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
        ('curriculum', '0007_lesson_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.userprofileinfo'),
        ),
    ]
