# Generated by Django 4.2.11 on 2024-05-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
