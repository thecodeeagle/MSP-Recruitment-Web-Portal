# Generated by Django 2.2.2 on 2019-07-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_portal', '0004_candidate_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
    ]
