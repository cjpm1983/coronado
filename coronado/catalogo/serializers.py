from catalogo.models import Catalogo
from rest_framework import serializers


class CatalogoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['id', 'autor', 'titulo', 'edicion', 'editorial', 'fecha_de_edicion', 'fecha', 'clasificacion', 'precio', 'adquisicion', 'proveedor', 'titulos', 'volumenes', 'baja', 'pais', 'ejemplares', 'tipo_documento', 'comentario']

    
