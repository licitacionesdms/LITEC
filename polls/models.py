# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class DispositivosMedicos(models.Model):
    id = models.AutoField(primary_key=True)
    referencia_fabricante = models.CharField(max_length=40, blank=True, null=True)
    referencia_lh = models.CharField(max_length=40,blank=True, null=True)
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
        managed = False  # Indica que no se administrará directamente en Django
        db_table = 'dispositivos_medicos'
        verbose_name = "Dispositivo Médico"
        verbose_name_plural = "Dispositivos Médicos"

    def save(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)  # Extrae el usuario si fue pasado en kwargs

        if self.pk:  # Solo se registra la trazabilidad si el objeto ya existe (actualización)
            old_instance = DispositivosMedicos.objects.get(pk=self.pk)
            
            for field in self._meta.fields:
                field_name = field.name
                old_value = getattr(old_instance, field_name)
                new_value = getattr(self, field_name)

                #if old_value != new_value:
                   # Trazabilidad.objects.create(
                    #    dispositivo=self,
                     #   usuario=usuario,
                      #  columna=field_name,
                       # dato_anterior=str(old_value),
                        #nuevo_dato=str(new_value),
                        #fecha_hora=now()
                   # )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.referencia_lh} - {self.marca} ({self.modelo})"

#class Trazabilidad(models.Model):
   # dispositivo = models.ForeignKey('DispositivosMedicos', on_delete=models.CASCADE)  # Relación con dispositivo
   # usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Usuario que hizo el cambio
   # columna = models.CharField(max_length=100)  # Columna modificada
   # dato_anterior = models.TextField()  # Valor anterior
   # nuevo_dato = models.TextField()  # Nuevo valor
   # fecha_hora = models.DateTimeField(auto_now_add=True)  # Fecha y hora del cambio


class Licitacion(models.Model):
    referencia_lh = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Referencia LH",
        help_text="Identificador único para cada licitación."
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )

    class Meta:
        verbose_name = "Licitación"
        verbose_name_plural = "Licitaciones"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.referencia_lh

class LicitacionDato(models.Model):
    licitacion = models.ForeignKey(
        Licitacion,
        on_delete=models.CASCADE,
        related_name='datos',
        verbose_name="Licitación"
    )
    campo = models.CharField(
        max_length=255,
        verbose_name="Nombre del campo"
    )
    valor = models.TextField(
        verbose_name="Valor del campo",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Dato de Licitación"
        verbose_name_plural = "Datos de Licitación"
        unique_together = ('licitacion', 'campo')  # Un campo único por licitación

    def __str__(self):
        return f"{self.licitacion.referencia_lh} - {self.campo}"


class AlertaVencimiento(models.Model):
    fabricante = models.CharField(max_length=200, verbose_name="Fabricante")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    registro_sanitario = models.CharField(max_length=30, verbose_name="Registro Sanitario")

    def _str_(self):
        return f"{self.nombre} - {self.fecha_vencimiento}"