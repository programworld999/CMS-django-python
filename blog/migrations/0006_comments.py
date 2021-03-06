# Generated by Django 2.1.5 on 2019-02-17 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=10)),
                ('website', models.CharField(max_length=10)),
                ('comment', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('postId', models.IntegerField()),
            ],
        ),
    ]
