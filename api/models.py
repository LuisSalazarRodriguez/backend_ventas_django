from django.db import models

from django.contrib.auth.models import User

class Linea(models.Model):
    linea_codigo = models.AutoField(primary_key=True)
    linea_nombre = models.CharField(max_length=100,verbose_name='nombre de linea')
    linea_estado = models.CharField(max_length=10,verbose_name='estado linea')
    
    def __str__(self):
        return self.linea_nombre
class Marca(models.Model):
    marca_codigo = models.AutoField(primary_key=True)
    marca_nombre = models.CharField(max_length=100,verbose_name='nombre de marca')
    marca_estado = models.CharField(max_length=10,verbose_name='estado marca')
    
    def __str__(self):
        return self.marca_nombre
    
class UnidadMedida(models.Model):
    um_codigo = models.AutoField(primary_key=True)
    um_descripcion = models.CharField(max_length=100,verbose_name='desscripcion de la unidad medida')
    um_estado = models.CharField(max_length=10,verbose_name='estado unidad medida')
    
    def __str__(self):
        return self.um_descripcion
    
class Moneda(models.Model):
    moneda_codigo = models.AutoField(primary_key=True)
    moneda_descripcion = models.CharField(max_length=100,verbose_name='desscripcion de la moneda')
    moneda_estado = models.CharField(max_length=10,verbose_name='estado moneda')
    
    def __str__(self):
        return self.moneda_descripcion
    
class Producto(models.Model):
    producto_codigo = models.AutoField(primary_key=True)
    producto_descripcion = models.CharField(max_length=100,verbose_name='desscripcion del producto')
    linea_codigo = models.ForeignKey(Linea,related_name='Producto',to_field='linea_codigo',on_delete=models.RESTRICT,db_column='linea_codigo',verbose_name='Linea')
    marca_codigo = models.ForeignKey(Marca,related_name='Producto',to_field='marca_codigo',on_delete=models.RESTRICT,db_column='marca_codigo',verbose_name='Marca')
    um_codigo = models.ForeignKey(UnidadMedida,related_name='Producto',to_field='um_codigo',on_delete=models.RESTRICT,db_column='um_codigo',verbose_name='UnidadMedida')
    producto_precio = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='precio del producto')
    moneda_codigo = models.ForeignKey(Moneda,related_name='Producto',to_field='moneda_codigo',on_delete=models.RESTRICT,db_column='moneda_codigo',verbose_name='Moneda')
    producto_estado = models.CharField(max_length=10,verbose_name='estado producto')
    producto_imagen = models.CharField(max_length=8000,verbose_name='imagen url producto',default='')
    
    def __str__(self):
        return self.producto_descripcion