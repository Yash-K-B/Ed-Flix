# Generated by Django 3.1.4 on 2021-05-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('file_text', models.TextField(max_length=10000000)),
            ],
        ),
    ]