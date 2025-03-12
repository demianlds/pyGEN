from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=100)
    actual_stock = models.PositiveIntegerField(default=0)
    min_stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.name

class Movimiento(models.Model):
    TYPES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    type = models.CharField(max_length=10, choices=TYPES)
    amount = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.product.name}"

