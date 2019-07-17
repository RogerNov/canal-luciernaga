# Generated by Django 2.2.3 on 2019-07-17 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0004_auto_20190715_0940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programacion',
            options={},
        ),
        migrations.RemoveField(
            model_name='programacion',
            name='hora',
        ),
        migrations.CreateModel(
            name='HoraProgramacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=225)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('programacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programacion.Programacion')),
            ],
            options={
                'verbose_name': 'Programación',
                'verbose_name_plural': 'Programaciones',
            },
        ),
    ]