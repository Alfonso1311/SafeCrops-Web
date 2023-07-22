from django.db import models

from django.contrib.auth.models import User #Libreria para usar la tabla usuarios por defecto de Django
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=1, related_name='usuario') #Se crea el campo user que es una relación uno a uno con el modelo User de django

    def __str__(self): #Se crea el método __str__ para que al momento de mostrar el objeto en la consola se muestre el nombre del usuario
        return f'Perfil de {self.user.username}' #Se retorna el nombre del usuario

    def delete(self, using=None, keep_parents=False): #Se sobreescribe el método delete para que no se elimine el usuario de django
        super().delete() #Se llama al método delete de la clase padre


class Administrador(models.Model): #Se crea el modelo Administrador
    id_Administrador = models.CharField(primary_key=True, max_length=15, verbose_name='ID_Administrador') #Se crea el campo id que es la llave primaria y es autoincrementable
    nombre = models.CharField(max_length=45, verbose_name='Nombre') #Se crea el campo nombre que es un campo de tipo cadena de caracteres
    apellidoP = models.CharField(max_length=45, verbose_name='Apellido P') #Se crea el campo apellidoP que es un campo de tipo cadena de caracteres
    apellidoM = models.CharField(max_length=45, verbose_name='Apellido M', null=True, blank=True, default='') #Se crea el campo apellidoM que es un campo de tipo cadena de caracteres
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha de Nacimiento', default=timezone.now) #Se crea el campo fechaNac que es un campo de tipo fecha
    correo = models.EmailField(max_length=50 ,verbose_name='Correo', null=True, blank=True, default='') #Se crea el campo correo que es un campo de tipo correo
    imagen = models.ImageField(max_length=100, upload_to='imagenes/', verbose_name='Imagen', default='imagenes/defaultProfile/defaultProfile.png') #Se crea el campo imagen que es un campo de tipo imagen
    userType = models.CharField(max_length=20, verbose_name='', default='Administrador') #Se crea el campo userType que es un campo de tipo cadena de caracteres
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ID_Usuario', related_name='administradorUser', null=True, blank=True) #Se crea el campo user que es una relación uno a uno con el modelo User de django
    

    def __str__(self): #Se crea el método __str__ para que al momento de mostrar el objeto en la consola se muestre el nombre del administrador
        fila = f'{self.user.username} - {self.nombre} {self.apellidoP}' #Se crea la variable fila que es una cadena de caracteres
        return fila #Se retorna la variable fila

    def delete(self, using=None, keep_parents=False): #Se sobreescribe el método delete para que no se elimine el usuario de django
        self.imagen.storage.delete(self.imagen.name)
        super().delete() #Se llama al método delete de la clase padre

class Experto(models.Model): #Se crea el modelo Experto
    id_Experto = models.AutoField(primary_key=True) #Se crea el campo id que es la llave primaria y es un campo autoincrementable
    nombre = models.CharField(max_length=45, verbose_name='Nombre') #Se crea el campo nombre que es un campo de tipo cadena de caracteres
    apellidoP = models.CharField(max_length=45, verbose_name='Apellido P') #Se crea el campo apellidoP que es un campo de tipo cadena de caracteres
    apellidoM = models.CharField(max_length=45, verbose_name='Apellido M', null=True, blank=True) #Se crea el campo apellidoM que es un campo de tipo cadena de caracteres
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha de Nacimiento', default=timezone.now) #Se crea el campo fechaNac que es un campo de tipo fecha
    correo = models.EmailField(max_length=50, verbose_name='Correo', null=True) #Se crea el campo correo que es un campo de tipo correo
    institucionPerteneciente = models.CharField(max_length=100, verbose_name='Institución a la que pertenece') #Se crea el campo correo que es un campo de tipo correo
    imagen = models.ImageField(max_length=100, upload_to='imagenes/', verbose_name='Imagen', default='imagenes/defaultProfile/defaultProfile.png') #Se crea el campo imagen que es un campo de tipo imagen
    userType = models.CharField(max_length=20, verbose_name='', default='Experto') #Se crea el campo userType que es un campo de tipo cadena de caracteres
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ID_Usuario', related_name='expertoUser', null=True, blank=True) #Se crea el campo user que es una relación uno a uno con el modelo User de django

    def __str__(self):  #Se crea el método __str__ para que al momento de mostrar el objeto en la consola se muestre el nombre del experto
        fila = "Nombre: " + self.nombre + " - " + " Apellido P: " + self.apellidoP
        return fila #Se retorna la variable fila

    def delete(self, using=None, keep_parents=False): #Se sobreescribe el método delete para que no se elimine el usuario de django
        self.imagen.storage.delete(self.imagen.name)
        super().delete() #Se llama al método delete de la clase padre

class Tester(models.Model): #Se crea el modelo Tester
    id_Tester = models.AutoField(primary_key=True) #Se crea el campo id que es la llave primaria y es un campo autoincrementable
    nombre = models.CharField(max_length=45, verbose_name='Nombre') #Se crea el campo nombre que es un campo de tipo cadena de caracteres
    apellidoP = models.CharField(max_length=45, verbose_name='Apellido P') #Se crea el campo apellidoP que es un campo de tipo cadena de caracteres
    apellidoM = models.CharField(max_length=45, verbose_name='Apellido M', null=True, blank=True)  #Se crea el campo apellidoM que es un campo de tipo cadena de caracteres
    fechaNac = models.DateField(auto_now_add=False, auto_now=False, blank=True ,verbose_name='Fecha de Nacimiento', default=timezone.now) #Se crea el campo fechaNac que es un campo de tipo fecha
    correo = models.EmailField(max_length=50, verbose_name='Correo', null=True)    #Se crea el campo correo que es un campo de tipo correo
    imagen = models.ImageField(max_length=100, upload_to='imagenes/', verbose_name='Imagen', default='imagenes/defaultProfile/defaultProfile.png') #Se crea el campo imagen que es un campo de tipo imagen
    userType = models.CharField(max_length=20, verbose_name='', default='Tester') #Se crea el campo userType que es un campo de tipo cadena de caracteres
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ID_Usuario', related_name='testerUser', null=True, blank=True) #Se crea el campo user que es una relación uno a uno con el modelo User

    def __str__(self):
        fila = self.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()