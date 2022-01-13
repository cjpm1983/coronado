# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalogo(models.Model):
    id = models.AutoField(primary_key=True,)
    #id = models.CharField(max_length=255,db_column='Id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inventario = models.CharField(max_length=255,db_column='Inventario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    autor = models.CharField(max_length=255,db_column='Autor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    titulo = models.CharField(max_length=255,db_column='Titulo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    edicion = models.CharField(max_length=255,db_column='Edicion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    editorial = models.CharField(max_length=255,db_column='Editorial', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha_de_edicion = models.CharField(max_length=255,db_column='Fecha de Edicion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    fecha = models.CharField(max_length=255,db_column='Fecha', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    clasificacion = models.CharField(max_length=255,db_column='Clasificacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    precio = models.CharField(max_length=255,db_column='Precio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adquisicion = models.CharField(max_length=255,db_column='Adquisicion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    proveedor = models.CharField(max_length=255,db_column='Proveedor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    titulos = models.CharField(max_length=255,db_column='Titulos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volumenes = models.CharField(max_length=255,db_column='Volumenes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    baja = models.CharField(max_length=255,db_column='Baja', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pais = models.CharField(max_length=255,db_column='Pais', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ejemplares = models.CharField(max_length=255,db_column='Ejemplares', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipo_documento = models.CharField(max_length=255,db_column='Tipo Documento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Catalogo'


# class Catalogo_Coronado(models.Model):
#     id = models.AutoField(primary_key=True,)
#     #id = models.CharField(max_length=255,db_column='Id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     inventario = models.CharField(max_length=255,db_column='Inventario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     autor = models.CharField(max_length=255,db_column='Autor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     titulo = models.CharField(max_length=255,db_column='Titulo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     edicion = models.CharField(max_length=255,db_column='Edicion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     editorial = models.CharField(max_length=255,db_column='Editorial', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     fecha_de_edicion = models.CharField(max_length=255,db_column='Fecha de Edicion', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
#     fecha = models.CharField(max_length=255,db_column='Fecha', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     clasificacion = models.CharField(max_length=255,db_column='Clasificacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     precio = models.CharField(max_length=255,db_column='Precio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     adquisicion = models.CharField(max_length=255,db_column='Adquisicion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     proveedor = models.CharField(max_length=255,db_column='Proveedor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     titulos = models.CharField(max_length=255,db_column='Titulos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     volumenes = models.CharField(max_length=255,db_column='Volumenes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     baja = models.CharField(max_length=255,db_column='Baja', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     pais = models.CharField(max_length=255,db_column='Pais', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     ejemplares = models.CharField(max_length=255,db_column='Ejemplares', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     tipo_documento = models.CharField(max_length=255,db_column='Tipo Documento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
#     comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'Catalogo_Coronado'

