# Generated by Django 4.0.4 on 2022-05-17 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostExperiencia', '0002_post_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cargo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
