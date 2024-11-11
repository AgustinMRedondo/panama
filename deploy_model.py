###############################
# This program lets you       #
# - Create a dashboard        #
# - Evevry dashboard page is  #
# created in a separate file  #
###############################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from ml import ml
from abstract import abstract


def main():

    #############
    # Main page #
    #############

    options = ['Inicio','Abstract', 'Modelo Predictivo RFC']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if choice == 'Inicio':
      st.title("Panamá")
      st.markdown("""
**Introducción**

Este proyecto busca analizar el mercado inmobiliario de Panamá, enfocado en la identificación de activos "distressed" o en riesgo de devaluación significativa. Para lograrlo, se emplea un enfoque basado en ciencia de datos y machine learning, utilizando un conjunto de datos históricos de precios por metro cuadrado, obtenidos a través de plataformas públicas. Mediante el uso del modelo de series temporales Prophet, se proyectan precios futuros hasta el 2028, proporcionando un contexto sobre la posible evolución del mercado en distintas zonas y tipologías de propiedades.

Posteriormente, se desarrolla un modelo predictivo utilizando un clasificador Random Forest, que permite determinar la probabilidad de que un activo esté "distressed". La metodología incluye la creación de un indicador de distress basado en la comparación entre el precio actual y las proyecciones futuras, así como una clasificación por zona y tipo de propiedad. Este modelo, entrenado y validado con datos históricos, busca ofrecer una herramienta precisa y aplicable para inversores y profesionales del sector inmobiliario.
""")
      st.image("images/pexels-jibarofoto-1494576.jpg")
      pass

    elif choice == 'Abstract':
      abstract()

    elif choice == 'Modelo Predictivo RFC':
      ml()

    else:
      st.stop()


main()
