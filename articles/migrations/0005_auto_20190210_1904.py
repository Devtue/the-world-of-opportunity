# Generated by Django 2.1.2 on 2019-02-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190210_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
