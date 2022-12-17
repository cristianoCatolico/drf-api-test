from django.db import models

class Pais(models.Model):
   nombre = models.CharField(max_length=20)
   moneda = models.CharField(max_length=20)
   creado_en = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.nombre

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    stock = models.IntegerField()

    def __str__(self):
       return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    done_at = models.DateField(null=True)
    updated_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(null=True)
    status = models.IntegerField(default=0)
