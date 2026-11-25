#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#opcion 1 con la opcion upload al inicio en Homa (opcion ue está junto a la opcion de vew file)
import pandas as pd
iris = pd.read_csv('Iris.csv')
iris


# In[ ]:


#Opcion 2
import os
import pandas as pd
os.chdir("/Users/User/Downloads")
iris = pd.read_csv('Iris.csv')
iris


# In[ ]:


iris_petal = iris[["petal.length", "petal.width"]]
iris_petal


# In[ ]:


#Exportacion, se pone el data frame, se pone el archivo en formato csv
iris_petal.to_csv('Iris_petal.cvs')
# aunque al ejecutarse no pase nada cuando ves en el directorio ahi se ve


# In[ ]:


# Histograma
iris['sepal.length'].hist()


# In[ ]:


subintervalos = int(round(len(iris)**0.5,0))
subintervalos
#Es un criterio para sacar los subintervalo ue es sacando la raiz cuadrada del numero de datos


# In[ ]:


iris['sepal.length'].hist(bins=subintervalos)


# In[ ]:


#diagrama de barras, primero sacamos la media
iris_tipo = iris.groupby('variety')['petal.length'].mean()
iris_tipo


# In[ ]:


#garfico de barras
iris_tipo.plot(kind ='bar')

