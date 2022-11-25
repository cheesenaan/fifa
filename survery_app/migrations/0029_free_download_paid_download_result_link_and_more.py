# Generated by Django 4.0.6 on 2022-10-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0028_coupon_attempts_after_expiry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='free_download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=500)),
                ('user_email', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='paid_download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=500)),
                ('user_email', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='link',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='attempts_after_expiry',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='attempts_after_limit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='value',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='affinity_Extrovert_to_Introvert',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='affinity_Introvert_to_Extrovert',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='collection_Intuition_to_Sensing',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='collection_Sensing_to_Intuition',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='make_Feeling_to_Thinking',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='make_Thinking_to_Feeling',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='time_Judging_to_Perceiving',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_choice_change',
            name='time_Perceiving_to_Judging',
            field=models.BigIntegerField(default=0),
        ),
    ]