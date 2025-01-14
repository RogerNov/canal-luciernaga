from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from lugar.models import Pais

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length =225)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Clasificacion(models.Model):
    nombre = models.CharField(max_length = 225)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Clasificacion"
        verbose_name_plural = "Clasificaciones"
        

TIPO_COMUNICACION_CHOICE = [
    (1, 'Noticia'),
    (2, 'Reportaje'),
]

class Comunicacion(models.Model):
    tipo = models.IntegerField(choices = TIPO_COMUNICACION_CHOICE)
    ultimo_momento = models.BooleanField()
    titulo = models.CharField(max_length = 225)
    clasificacion = models.ForeignKey(Clasificacion, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    autor = models.CharField(max_length = 255)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='fotos/noticias')
    descripcion = models.TextField(max_length = 225)
    pais = models.ForeignKey(Pais, on_delete = 255)
    fuente = models.CharField(max_length = 225)
    tags = TaggableManager()
    slug = models.SlugField(max_length=250, unique=True, editable= False)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Noticia/Reportaje"
        verbose_name_plural = "Noticias/Reportajes"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Comunicacion, self).save(*args, **kwargs)
    