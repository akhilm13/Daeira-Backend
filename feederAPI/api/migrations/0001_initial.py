# Generated by Django 2.0.3 on 2018-03-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinksTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
