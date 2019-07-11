# Generated by Django 2.2.3 on 2019-07-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tematicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='noticias',
            name='autor',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticias',
            name='foto',
            field=models.ImageField(default='', upload_to='fotos/noticias'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticias',
            name='tematica',
            field=models.ManyToManyField(to='noticias.Tematicas'),
        ),
    ]