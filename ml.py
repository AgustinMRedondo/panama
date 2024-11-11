# Import python libraries
import pickle
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


def ml():
    st.title("Acceso al Modelo Predictivo")

    # Define la contraseña
    PASSWORD = "credere"

    # Solicitar la contraseña al usuario
    input_password = st.text_input("Introduce la contraseña:", type="password")

    # Verificar la contraseña
    if input_password == PASSWORD:
        st.success("Contraseña correcta. Acceso concedido.")
        st.title("Modelo predictivo de distressed Panamá 2024-2028")

        # loading the model
        models_path = 'models/'
        model_name = models_path + 'rfc.pkl'
        loaded_model = pickle.load(open(model_name, 'rb'))

        # loading the encoder
        encoders_path = 'encoders/'
        encoder_name = encoders_path + 'encoder.pkl'
        loaded_encoder = pickle.load(open(encoder_name, 'rb'))

        # Lists of accptable values
        zonas_validas = ['Panamá', 'Arraiján', 'Chame', 'Nueva Gorgona', 'Otro', 'Río Hato', 'San Carlos', 'San José', 'San Miguelito']
        tipos_validos = ['Piso', 'Casa']

        # Get input values.
        precio = st.number_input("Precio de la unidad en USD o PAB: ", 10000, 50000000)
        habitaciones = st.number_input("Numero de habitaciones: ", 0, 30)
        banos = st.number_input("Numero de baños: ", 0, 30)
        area = st.number_input("M2 de la unidad ", 0, 10000)
        zona = st.selectbox("Zona", zonas_validas, key = "3")
        tipo = st.selectbox("Tipología del activo ",tipos_validos, key = '2')
    

        # when 'Predict' is clicked, make the prediction and store it
        if st.button("Consigue tu predicción"):

            # Crear entrada de datos
            X = pd.DataFrame({'Price': [precio],
                          'Bedrooms': [habitaciones],
                          'Bathrooms': [banos],
                          'area': [area],
                          'Location': [zona],
                          'Type': [tipo]})

            # Procesamiento de variables
            numerical = X.select_dtypes(include=np.number)
            categorical = X.select_dtypes(include=object)

            column_names = ['Location_Arraiján', 'Location_Chame', 'Location_Nueva Gorgona',
                        'Location_Otro', 'Location_Panamá', 'Location_Río Hato',
                        'Location_San Carlos', 'Location_San José', 'Location_San Miguelito',
                        'Type_Casa', 'Type_Piso']
            cat_transformed = loaded_encoder.transform(categorical).toarray()
            categorical = pd.DataFrame(cat_transformed, columns=column_names)
        
            # Unir dataframes
            X = pd.concat([numerical, categorical], axis=1)

            # Predicción inicial
            prediction = loaded_model.predict(X)
            prediction_probs = loaded_model.predict_proba(X)

            # Mostrar predicción inicial
            if prediction == 1:
                st.success("DISTRESSED: El modelo predice que el activo está Distressed con una probabilidad de {:.2f}".format(prediction_probs[0,1]))
            else:
                st.error("NO DISTRESSED: El modelo predice que el activo NO está Distressed con una probabilidad de {:.2f}".format(prediction_probs[0,0]))

            # Crear rango de precios para tramos de 10000
            precios = [precio + i * 10000 for i in range(-20, 21)]
            probabilidades = []

            # Calcular probabilidad de distress para cada precio en el rango
            for p in precios:
                X['Price'] = p
                prediction_probs = loaded_model.predict_proba(X)
                probabilidades.append(prediction_probs[0, 1])

            # Determinar el precio de inflexión (cuando la probabilidad baja de 0.9)
            precio_inflexion = None
            for p, prob in zip(precios, probabilidades):
                if prob < 0.9:
                    precio_inflexion = p
                    break

            # Mostrar gráfico de probabilidades según el precio
            st.write("Probabilidades de 'Distressed' en función del precio:")
            plt.figure(figsize=(10, 5))
            plt.plot(precios, probabilidades, marker='o')
            plt.axhline(0.9, color='red', linestyle='--', linewidth=1, label='Probabilidad 0.9')
            plt.xlabel("Precio en USD")
            plt.ylabel("Probabilidad de Distressed")
            plt.title("Probabilidad de Distressed según variación de Precio")
            plt.legend()
            st.pyplot(plt)

            # Mostrar el precio de inflexión
            if precio_inflexion:
                st.write(f"El precio de esta casa debería ser aproximadamente **{precio_inflexion} USD** para que la probabilidad de distress baje de 0.9.")
            else:
                st.write("No se encontró un punto de inflexión en el rango de precios analizado.")
        else:
            st.error("Contraseña incorrect.a. Inténtalo de nuevo")
