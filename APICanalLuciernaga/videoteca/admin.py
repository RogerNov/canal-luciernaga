from django.contrib import admin
from .models import Video, Director, Tipo, Categoria, Episodio, Temporada
from lugar.models import Pais
import nested_admin


class TipoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class EpisodioInline(nested_admin.NestedTabularInline):
    model = Episodio
    extra = 1

class TemporadaInline(nested_admin.NestedStackedInline):
    model = Temporada
    extra = 1
    inlines = [EpisodioInline]


class VideoAdmin(nested_admin.NestedModelAdmin):
    autocomplete_fields = ['tipo','director','categoria', 'pais']
    inlines = [TemporadaInline,]

    class Media:
        js = ('js/video/ocultar.js',)
    

# Register your models here.
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Director,DirectorAdmin) 
admin.site.register(Video,VideoAdmin)  