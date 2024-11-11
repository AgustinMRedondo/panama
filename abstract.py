# Import python libraries
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


def abstract():
    st.markdown("""
**Abstract**

Este proyecto se centra en un análisis exhaustivo de datos para estudiar las variaciones de precios en el mercado inmobiliario de Panamá. Utilizando un algoritmo de series temporales (Prophet), se realiza una proyección de precios a futuro, permitiendo identificar el rango en el que un activo puede considerarse "distressed" desde el presente hasta el 2028. A partir de esta información, se emplea un clasificador Random Forest para desarrollar un modelo predictivo que, basado en datos básicos independientes, determine la probabilidad de que un activo esté o no en situación de distressed.

**Evolución de los precios**

Para obtener un histórico de la evolución de precios en Panamá, se recopilan datos de properstar.es, que ofrece información sobre el precio por metro cuadrado desde 2021 hasta octubre de 2024. Con estos datos, se construye un registro histórico de precios de pisos y casas, analizando las variaciones mensuales en este período. Además, se incluye una diferenciación por zonas, ajustando la variación mensual de cada área para proyectar datos de precios hasta 2021, estableciendo así una base de comparación de valores.

**Prophet**

Con el dataset histórico de precios se aplica el algoritmo de series temporales Prophet, que permite modelar la evolución de precios a lo largo del tiempo, detectando patrones estacionales y fluctuaciones. Este análisis revela, por ejemplo, una tendencia negativa recurrente en el mes de diciembre, lo cual es representativo de la variabilidad temporal de este mercado. Prophet facilita la proyección de precios por tipología de propiedad y zonas geográficas hasta el año 2028. Aunque las proyecciones no se pueden verificar a futuro, este modelo permite identificar tendencias generales del mercado.

**Creación de datos para entrenar el modelo predictivo**

A partir de los datos generados, se procede a aplicar los valores proyectados a 1,746 propiedades obtenidas mediante scraping en properstar.es. Comparamos el precio actual por metro cuadrado con las proyecciones de precios de 2024 a 2028, generando un indicador de "distressed" según la tipología de propiedad (piso o casa) y la zona geográfica. Si el precio actual por metro cuadrado de una vivienda es inferior al precio proyectado en un periodo t, se asigna un punto; lo mismo ocurre si el precio está por debajo del rango proyectado para su zona. Al sumar estas puntuaciones hasta 2028, si la suma total es superior a 8, el activo se clasifica como distressed (1); de lo contrario, se clasifica como no distressed (0).

**Desarrollo del modelo predictivo**

Con los datos generados, se entrena un clasificador Random Forest, cuyo objetivo es predecir la probabilidad de que un activo esté o no distressed. Entrenado con el 80% de los datos, el modelo alcanza una precisión del 92% sobre el 20% restante, demostrando su efectividad para identificar activos distressed con una alta fiabilidad.

Se implementa además una iteración en tramos de -10,000 a +10,000 en el precio del activo para analizar cómo varía la probabilidad de que esté distressed. Este análisis permite identificar el precio a partir del cual la probabilidad de distress baja del 90%, estableciendo así un "punto de inflexión" que indica el valor real del activo.

**Limitaciones**

La precisión del modelo está intrínsecamente ligada a las suposiciones realizadas en la creación del dataset de entrenamiento. 

**Puntos fuertes**: Los datos históricos desde 2021 permiten observar la tendencia del mercado, y el uso de Prophet proporciona una buena aproximación a las variaciones a largo plazo. La combinación de modelos Prophet y Random Forest permite realizar análisis de tendencias y rangos de valores para los activos.

**Puntos débiles**: Los datos disponibles son limitados y no han sido verificados por entidades reguladas, lo que podría afectar la fiabilidad de los resultados.
""")


