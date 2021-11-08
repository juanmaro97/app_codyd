# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TipoContacto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tipo_contacto'


class Contacto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cedula_nit = models.CharField(db_column='Cedula_NIT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    id_tipo_contacto = models.ForeignKey('TipoContacto', models.DO_NOTHING, db_column='id_TipoContacto')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'contacto'


class DetalleFacturacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    facturacion = models.ForeignKey('Facturacion', models.DO_NOTHING, db_column='Facturacion_ID')  # Field name made lowercase.
    inventario_id_productos = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='Inventario_ID_productos')  # Field name made lowercase.
    subtotal = models.FloatField(db_column='Subtotal', blank=True, null=True)  # Field name made lowercase.
    descuento = models.FloatField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.PositiveIntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'detalle_facturacion'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         # managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         # managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         # managed = False
#         db_table = 'django_session'


class Facturacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='contacto_ID')  # Field name made lowercase.
    fecha_orden = models.DateField(db_column='Fecha_orden', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total = models.PositiveIntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    tipo_pago = models.CharField(db_column='Tipo_pago', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'facturacion'


class Inventario(models.Model):
    id_productos = models.AutoField(db_column='ID_productos', primary_key=True)  # Field name made lowercase.
   # proveedores = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='Proveedores_ID')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precio_unitario = models.PositiveIntegerField(db_column='Precio_unitario', blank=True, null=True)  # Field name made lowercase.
    cant_stock = models.PositiveIntegerField(db_column='Cant_stock', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'inventario'


