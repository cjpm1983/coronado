from catalogo.models import Catalogo, Catalogo_Coronado
from rest_framework import serializers


class CatalogoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['id', 'autor', 'titulo', 'edicion', 'editorial', 'fecha_de_edicion', 'fecha', 'clasificacion', 'precio', 'adquisicion', 'proveedor', 'titulos', 'volumenes', 'baja', 'pais', 'ejemplares', 'tipo_documento', 'comentario']

class CatalogoCoronadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogo_Coronado
        fields = ['id', 'fecha_adquisicion', 'no_registro', 'autor', 'titulo', 'edicion', 'editorial', 'ano_de_publicacion', 'proveedor', 'sala', 'cantidad_titulos', 'ejemplares', 'pais', 'idioma', 'tipo_documento', 'precio', 'via_adquisicion', 'clasificacion', 'notas', 'baja', 'editorial', 'estado_conservacion', 'materia', 'volumenes']
  



