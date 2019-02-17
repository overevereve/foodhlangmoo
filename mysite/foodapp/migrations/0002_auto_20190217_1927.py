# Generated by Django 2.1.4 on 2019-02-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail_res',
            name='topic_review',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='route',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='detail_res',
            name='review_text',
            field=models.CharField(max_length=300),
        ),
    ]