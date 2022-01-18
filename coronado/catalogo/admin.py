from django.contrib import admin
from .models import Catalogo
from .models import Catalogo_Coronado

# Register your models here.

def download_csv(modeladmin, request, queryset):
    import csv
    f = open('some.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(['titulo','autor','edicion','editorial','tipo_documento', 'clasificacion'])
    for s in queryset:
        writer.writerow([s.titulo, s.autor,s.edicion, s.editorial, s.tipo_documento, s.clasificacion])

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ( 'titulo','autor','edicion','editorial','tipo_documento', 'clasificacion')
    list_filter = ['tipo_documento']
    search_fields = ['titulo','autor', 'editorial']
    actions = [download_csv]

@admin.register(Catalogo_Coronado)
class CatalogoCoronadoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ( 'titulo','autor','edicion','editorial','tipo_documento', 'clasificacion')
    list_filter = ['tipo_documento']
    search_fields = ['titulo','autor', 'editorial']
    actions = [download_csv]

#admin.site.register(Catalogo, CatalogoAdmin)


