# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DispositivosMedicos(models.Model):
    referencia_fabricante = models.CharField(max_length=40, blank=True, null=True)
    referencia_lh = models.CharField(max_length=40, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    descripcion_espanol = models.TextField(blank=True, null=True)
    descripcion_ingles = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=250, blank=True, null=True)
    nombre_registro_sanitario = models.CharField(max_length=200, blank=True, null=True)
    registro_sanitario = models.CharField(max_length=30)
    no_resolucion = models.CharField(max_length=20, blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    alerta_vencimiento = models.CharField(max_length=10, blank=True, null=True)
    expediente = models.CharField(max_length=20, blank=True, null=True)
    radicado = models.CharField(max_length=20, blank=True, null=True)
    modalidad = models.CharField(max_length=50, blank=True, null=True)
    titular_registro_sanitario = models.CharField(max_length=200, blank=True, null=True)
    fabricante = models.CharField(max_length=200, blank=True, null=True)
    direccion_fabricante = models.TextField(blank=True, null=True)
    importador = models.CharField(max_length=100, blank=True, null=True)
    acondicionador = models.CharField(max_length=100, blank=True, null=True)
    material_fabricacion = models.TextField(blank=True, null=True)
    clasificacion_riesgo = models.CharField(max_length=20, blank=True, null=True)
    vida_util_anos = models.CharField(max_length=40, blank=True, null=True)
    vida_util_meses = models.CharField(max_length=20, blank=True, null=True)
    presentacion_comercial = models.TextField(blank=True, null=True)
    condiciones_almacenamiento = models.TextField(blank=True, null=True)
    tipo_dispositivo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_medicos'
