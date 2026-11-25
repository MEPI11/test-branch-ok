#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numero1= Complejo(2,3)
numero2 = Complejo(3,4)
suma = numero1.agregar(numero2)
print("parte real",suma.real)
print("parte imagianria", suma.imaginario)


# In[ ]:


# de puede borrar con del
del numero1
numero1


# In[ ]:


# la referencia self puede tomar cualquier otra denominación
class Persona:
    def __init__(objeto, nombre,edad):
        objeto.nombre = nombre
        objeto.edad = edad
    def mensaje(objeto):
        print ("hola mi nombre es: " + objeto.nombre)

personal = Persona("Juan",35)
personal.mensaje()


# Ejercicio:
# Crea una clase denominada “Triangulo”. Crea un objeto
# a partir de dicha clase, el cual deberá tener los atributos a, b y c
# que representan los lados de dicho triángulo.
# La clase “Triangulo” deberá tener 2 métodos:
# 1) El constructor init se usará para inicializar los lados
# del triángulo
# 2) El método perim que deberá usarse para calcular
# el perímetro total del triángulo
# El perímetro del triángulo deberá ser impreso
# desde fuera de la clase.

# In[ ]:


class Triangulo:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perim(self):
        return self.a + self.b+ self.c
triangulo1 = Triangulo(2,3,4)
perimetro1 = triangulo1.perim()
print(perimetro1)    

