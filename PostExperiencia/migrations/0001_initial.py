# Generated by Django 4.0.4 on 2022-05-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('inicio', models.DateTimeField()),
                ('final', models.DateTimeField()),
            ],
        ),
    ]
