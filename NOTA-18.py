#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
arreglo = np.array([['Bella', 'Labrador', 'Cafe', 56, 24, '2013-07-01'],
                    ['Charlie', 'Poodle', 'Negro', 43, 24, '2016-09-16'],
                     ['Lucy', 'Chow-chow', 'Cafe', 46, 24, '2014-08-25'],
                      ['Cooper', 'Schnauzer', 'Gris', 49,17, '2011-12-11'],
                       ['Bernie', 'San Bernardo', 'Blanco', 77, 74, '2018-02-27'],
                   ['Max', 'Chow-chow', 'Blanco', 45, 26, '2019-03-27'], 
                    ['Reed', 'Schnauzer','Negro',45,15, '2017-09-18']])
arreglo


# In[ ]:


import pandas as pd 
df = pd.DataFrame(data=arreglo, columns =['Nombre', 'Raza','Color',  'Altura_cm', 'Peso_kg', 'Fecha_Nac'])
df ['Peso_kg'] = df['Peso_kg'].astype(int)
df ['Altura_cm'] = df['Altura_cm'].astype(int)
df


# In[ ]:


# MEdia o pormedio para el peso de las mascotas
df['Peso_kg'].mean()


# In[ ]:


df['Fecha_Nac'].min()


# In[ ]:


# Funcion de agregaci´n estadistica
def percentil80(columna):
    return columna.quantile(0.80)
df['Altura_cm'].agg(percentil80)


# In[ ]:


# Agrupacion estadistica en varias columnas
df[['Altura_cm','Peso_kg']].agg(percentil80)


# In[ ]:


# Funcion de agregacion Multiple
def percentil90(columna):
    return columna.quantile(0.90)
df['Altura_cm'].agg([percentil80,percentil90])


# In[ ]:


df['Altura_cm']


# In[ ]:


df['Altura_cm'].cumsum() # va sumando 


# In[ ]:


df['Altura_cm'].cummin() # va viendo el menor


# In[ ]:


# Conteo de perros por raza
df['Raza'].value_counts()


# In[ ]:


# Proporcion de perros por raza
df['Raza'].value_counts(normalize=True)
# frecuencia/ el total osea frecuencia relativa


# In[ ]:


# peso segun color
print(df[df['Color']=='Blanco']['Peso_kg'].mean())
print(df[df['Color']=='Cafe']['Peso_kg'].mean())
print(df[df['Color']=='Gris']['Peso_kg'].mean())
print(df[df['Color']=='Negro']['Peso_kg'].mean())


# In[ ]:


# Resumen por grupo; mejor opcion asi es más rapido que el ejemplo de arriba
df.groupby('Color')['Peso_kg'].mean()


# In[ ]:


#Agrupacion por color en base a diversas estadisticas
df.groupby('Color')['Peso_kg'].agg([min, max, sum])


# In[ ]:


# Agrupación por color raza en base a la media del peso
df.groupby(['Color','Raza'])['Peso_kg'].mean()


# In[ ]:


# Usoo de tablas pivote
df.pivot_table(values = 'Peso_kg', index = 'Color', aggfunc = [np.mean, np.median])


# In[ ]:


# Obtención de promedio para 2 variables
df.pivot_table(values = 'Peso_kg', index = 'Color', columns = 'Raza') # media se toma por omision


# In[ ]:


# Obtención de promedios para 2 variables Mejora #1
df.pivot_table(values = 'Peso_kg', index = 'Color', columns = 'Raza', fill_value = 0)


# In[ ]:


#Obtencion de promedios para dos variables: mejora #2
df.pivot_table(values = 'Peso_kg', index = 'Color', columns = 'Raza', fill_value =0, margins = True, aggfunc = np.mean) 


# In[ ]:


# Obtencion de media para dos variables
df.pivot_table(values = 'Peso_kg', index = 'Color', columns = 'Raza', fill_value =0, margins = True, aggfunc = np.median) 

