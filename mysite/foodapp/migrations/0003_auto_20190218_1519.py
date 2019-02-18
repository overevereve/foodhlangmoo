# Generated by Django 2.1.4 on 2019-02-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_auto_20190217_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_review', models.CharField(default='', max_length=120)),
                ('point', models.IntegerField(default=0)),
                ('review_text', models.CharField(max_length=300)),
                ('date_review', models.DateTimeField(verbose_name='date published')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurants')),
            ],
        ),
        migrations.RemoveField(
            model_name='detail_res',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Detail_res',
        ),
    ]
