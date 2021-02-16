# Generated by Django 3.1.1 on 2020-09-26 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='lesson',
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='standard',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
