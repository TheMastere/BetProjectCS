# Generated by Django 2.0.13 on 2019-07-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cesvcurrentmatchs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Left_team_title', models.CharField(max_length=50)),
                ('Left_team_coefficients', models.CharField(max_length=50)),
                ('Moneybet_for_left_team', models.CharField(max_length=50)),
                ('Left_team_win_percent', models.CharField(max_length=50)),
                ('Time_before_match', models.CharField(max_length=50)),
                ('Right_team_title', models.CharField(max_length=50)),
                ('Right_team_coefficients', models.CharField(max_length=50)),
                ('Moneybet_for_right_team', models.CharField(max_length=50)),
                ('Right_team_win_percent', models.CharField(max_length=50)),
            ],
        ),
    ]
