# Generated by Django 4.0.4 on 2022-05-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostExperiencia', '0007_post_linkempresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ubicación'),
        ),
    ]
