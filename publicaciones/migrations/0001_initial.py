# Generated by Django 4.2.6 on 2023-10-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('status', models.SmallIntegerField()),
                ('publishedDate', models.DateTimeField()),
            ],
        ),
    ]
