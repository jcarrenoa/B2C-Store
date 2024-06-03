from django.db import models
from auth_b2c.models import Perfil

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

    class Meta: 
        verbose_name = 'categoria'
        verbose_name_plural = "Categorias"
        db_table = "Categoria"
    
class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    ProductoOfrecido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='proveedor', null=True)
    
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "Proveedor"

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Tamaño = models.CharField(max_length=50, null=True)
    Descripcion = models.CharField(max_length=500, null=True, default="Aun no se tiene informacion del prodcuto.")
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return f'Producto: {self.Nombre} - Proveedor: {self.idProveedor.Nombre}'

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "Producto"

class Descuento(models.Model):
    idDescuento = models.AutoField(primary_key=True)
    PorcentajeDesc = models.IntegerField()
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='descuentos', null=True)

    def __str__(self):
        return f'idDescuento = {self.idDescuento}'

    class Meta:
        verbose_name = "Descuento"
        verbose_name_plural = "Descuentos"
        db_table = "Descuento"

class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    NroParticipantes = models.IntegerField()
    Beneficio = models.CharField(max_length=50)
    Mensaje = models.CharField(max_length=500)
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    imagen = models.ImageField(upload_to='eventos', null=True)

    def __str__(self):
        return f"Evento id: {self.idEvento}"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        db_table = "Evento"

class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    idPerfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return f'idCarrito = {self.idCarrito} - idPerfil = {self.idPerfil}'

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
        db_table = "Carrito"

class DetallesCarrito(models.Model):
    idDetallesCarrito = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField()
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idCarrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

    def __str__(self):
        return f'idDetallesCarrito = {self.idDetallesCarrito} - idProducto = {self.idProducto} - idCarrito = {self.idCarrito}'

    class Meta:
        verbose_name = "DetallesCarrito"
        verbose_name_plural = "DetallesCarritos"
        db_table = "DetallesCarrito"

class Orden(models.Model):
    idOrden = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Total = models.FloatField()
    Estado = models.BooleanField()
    idPerfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    ArchivoPDF = models.FileField(upload_to='facturas/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'idOrden = {self.idOrden} - idPerfil = {self.idPerfil}'

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
        db_table = "Orden"

class Mensaje(models.Model):
    idMensaje = models.AutoField(primary_key=True)
    Asunto = models.CharField(max_length=50)
    Mensaje = models.CharField(max_length=400)
    Fecha = models.DateField()
    idPerfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return f'idMensaje = {self.idMensaje} - idPerfil = {self.idPerfil}'

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        db_table = "Mensaje"