# Generated by Django 2.0.13 on 2019-07-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cesvpastmatchs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cesvpastmatchs',
            name='Moneybet_for_left_team',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cesvpastmatchs',
            name='Moneybet_for_right_team',
            field=models.CharField(max_length=50),
        ),
    ]