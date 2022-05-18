# Generated by Django 4.0.4 on 2022-05-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostExperiencia', '0003_post_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('nacionalidad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nacionalidad')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True, verbose_name='Teléfono')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
                ('github', models.URLField(blank=True, null=True, verbose_name='Github')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Biografía')),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, verbose_name='Habilidad')),
                ('porcentaje', models.IntegerField(verbose_name='Nivel de conocimiento (Hasta 6)')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Descripción del puesto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cargo',
            field=models.CharField(max_length=100, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='empresa',
            field=models.CharField(max_length=200, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='post',
            name='final',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de finalización'),
        ),
        migrations.AlterField(
            model_name='post',
            name='inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Logo de la empresa'),
        ),
    ]