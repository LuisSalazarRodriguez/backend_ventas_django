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
    
class Ubigeo(models.Model):
    ubigeo_codigo = models.AutoField(primary_key=True)
    ubigeo_departamento = models.CharField(max_length=50,verbose_name='ubigeo_departamento')
    ubigeo_provincia = models.CharField(max_length=50,verbose_name='ubigeo_provincia')
    ubigeo_distrito = models.CharField(max_length=50,verbose_name='ubigeo_distrito')
    
    def __str__(self):
        return self.ubigeo_departamento + "-" + self.ubigeo_provincia + "-" + self.ubigeo_distrito

class Tipo_documento(models.Model):
    tipodoc_codigo = models.AutoField(primary_key=True)
    tipodoc_descripcion = models.CharField(max_length=100,verbose_name='tipodoc_descripcion')
    tipodoc_estado = models.CharField(max_length=10,verbose_name='tipodoc_estado')
    
    def __str__(self):
        return self.tipodoc_descripcion

class Clientes(models.Model):
    clientes_codigo = models.AutoField(primary_key=True)
    tipodoc_codigo = models.ForeignKey(Tipo_documento,related_name='Clientes',to_field='tipodoc_codigo',on_delete=models.RESTRICT,db_column='tipodoc_codigo',verbose_name='Tipo_documento')
    clientes_numdoc = models.CharField(max_length=100,verbose_name=' cliente_numdoc')
    clientes_nombres = models.CharField(max_length=50,verbose_name='cliente_nombres')
    clientes_apellidos = models.CharField(max_length=50,verbose_name='cliente_apellidos')
    clientes_razonsocial = models.CharField(max_length=100,verbose_name='cliente_razonsocial')
    ubigeo_codigo = models.ForeignKey(Ubigeo,related_name='Clientes',to_field='ubigeo_codigo',on_delete=models.RESTRICT,db_column='ubigeo_codigo',verbose_name='Ubigeo')
    clientes_telefono = models.CharField(max_length=20,verbose_name='cliente_telefono')
    clientes_direccion = models.CharField(max_length=100,verbose_name='cliente_direccion')
    clientes_estado = models.CharField(max_length=10,verbose_name='cliente_estado')
    
    def __str__(self):
        return str(self.clientes_codigo)

class Pedido(models.Model):
    pedido_codigo = models.AutoField(primary_key=True)
    clientes_codigo = models.ForeignKey(Clientes,related_name='Pedido',to_field='clientes_codigo',on_delete=models.RESTRICT,db_column='clientes_codigo',verbose_name='Clientes')
    pedido_subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido subtotal')
    pedido_igv = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido igv')
    pedido_total = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido total')
    pedido_estado = models.CharField(max_length=10,verbose_name='estado pedido')
    
    def __str__(self):
        return str(self.pedido_codigo)
    
class PedidoDetalle(models.Model):
    pedidodetalle_codigo = models.AutoField(primary_key=True)
    pedido_codigo = models.ForeignKey(Pedido,related_name='PedidoDetalle',to_field='pedido_codigo',on_delete=models.RESTRICT,db_column='pedido_codigo',verbose_name='Pedido')
    producto_codigo = models.ForeignKey(Producto,related_name='PedidoDetalle',to_field='producto_codigo',on_delete=models.RESTRICT,db_column='producto_codigo',verbose_name='Producto')
    pedidodetalle_precio = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido detalle precio')
    pedidodetalle_cantidad = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido detalle cantidad')
    pedidodetalle_subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido detalle sub total')
    pedidodetalle_total = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='pedido detalle total')
    pedidodetalle_estado = models.CharField(max_length=10,verbose_name='estado pedido detalle')
    
    def __str__(self):
        return str(self.pedidodetalle_codigo)