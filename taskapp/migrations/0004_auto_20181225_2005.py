# Generated by Django 2.0.9 on 2018-12-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_remove_file_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.CharField(default='p', max_length=2),
        ),
        migrations.AddField(
            model_name='file',
            name='userid',
            field=models.IntegerField(default=1),
        ),
    ]
