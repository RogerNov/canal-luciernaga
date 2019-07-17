# Generated by Django 2.2.3 on 2019-07-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_remove_clasificacion_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comunicacion',
            options={'verbose_name': 'Noticia/Reportaje', 'verbose_name_plural': 'Noticias/Reportajes'},
        ),
        migrations.AlterField(
            model_name='comunicacion',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Noticia'), (2, 'Reportaje')]),
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]