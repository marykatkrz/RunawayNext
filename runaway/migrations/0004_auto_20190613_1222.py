# Generated by Django 2.2.1 on 2019-06-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runaway', '0003_auto_20190613_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]