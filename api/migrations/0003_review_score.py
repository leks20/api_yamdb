# Generated by Django 3.0.5 on 2020-05-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200501_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]
