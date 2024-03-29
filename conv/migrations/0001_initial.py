# Generated by Django 2.2.4 on 2019-08-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prodId', models.AutoField(primary_key=True, serialize=False)),
                ('prodName', models.CharField(max_length=255, unique=True)),
                ('prodType', models.CharField(max_length=20)),
                ('prodEventType', models.CharField(max_length=20)),
                ('prodPrice', models.PositiveIntegerField()),
                ('prodImg', models.URLField(null=True)),
            ],
            options={
                'ordering': ['prodName'],
            },
        ),
    ]
