# Generated by Django 4.0.6 on 2022-09-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0015_result_four_letter_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pdf_free',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='pdf_paid',
            field=models.CharField(default=-1, max_length=500),
            preserve_default=False,
        ),
    ]
