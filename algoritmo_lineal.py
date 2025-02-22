import streamlit as st
import pandas as pd

# Configuración para pantalla completa
st.set_page_config(layout="wide")

# Función para realizar las operaciones
def algoritmo_lineal(semilla, constanteA, constanteC, constanteM, iteraciones):
    # Lista para almacenar los resultados
    resultados = []
    
    for i in range(iteraciones):
        # Calculo de algoritmo lineal
        Ni = ((semilla * constanteA) + constanteC) % constanteM
        
        # Calculo del número psedoaleatorio
        Ri = Ni / (constanteM - 1)
       
        # Guardamos los resultados en una lista
        resultados.append({
            'Iteración': i+1,
            'Semilla': semilla,
            'A': constanteA,
            'C': constanteC,
            'M': constanteM,
            'Ni': Ni,
            'Ri': Ri
        })
        
        # La nueva semilla será el valor de Ni
        semilla = Ni
        
    return resultados
    
# Interfaz gráfica con Streamlit
st.title("Generador Producto Medio")

# Crear columnas para organizar el diseño (entrada en la izquierda y resultados en la derecha)
col1, espacio, col2 = st.columns([2, 0.5, 3])

# Captura de datos
with col1:
    semilla_input = st.number_input("Ingresa la semilla (número de dígitos pares y mayor a 0):", min_value = 0, step = 1)
    constanteA_input = st.number_input("Ingresa la constante A (número de dígitos pares y mayor a 0):", min_value = 0, step = 1)
    constanteC_input = st.number_input("Ingresa la constante C (número de dígitos pares y mayor a 0):", min_value = 0, step = 1)
    constanteM_input = st.number_input("Ingresa la constante M (número de dígitos pares y mayor a 0):", min_value = 0, step = 1)
    iteraciones_input = st.number_input("Ingresa las iteraciones:", min_value = 0, step = 1)

# Si ambos inputs están llenos, hacer las validaciones y mostrar los resultados
if semilla_input and constanteA_input and constanteC_input and constanteM_input and iteraciones_input:
    try:
        semilla = int(semilla_input)  # Convertir la semilla a entero
        constanteA = int(constanteA_input)  # Convertir la constanteA a entero
        constanteM = int(constanteM_input)  # Convertir la constanteM a entero
        constanteC = int(constanteC_input)  # Convertir la constanteC a entero
        iteraciones = int(iteraciones_input)  # Convertir las iteraciones a entero

        # Validación de las condiciones de entrada
        if semilla > 0 and len(str(semilla)) % 2 == 0 and constanteA > 0 and len(str(constanteA)) % 2 == 0 and constanteM > 0 and constanteC > 0 and len(str(constanteC)) % 2 == 0 and iteraciones > 0 and len(str(semilla)) == len(str(constanteA)) == len(str(constanteC)):
            # Obtener los resultados de las operaciones
            resultados = algoritmo_lineal(semilla, constanteA, constanteC, constanteM, iteraciones)
            
            # Convertir la lista de resultados en un DataFrame de Pandas
            df = pd.DataFrame(resultados)
            
            # Eliminando una columna 
            df = df.drop(df.columns[0], axis=1)  # Elimina la primera columna
                        
            # Mostrar la tabla en la columna derecha
            with col2:
                st.header("Tabla Generada")
                st.dataframe(df, use_container_width=True)
                
                with st.expander("Hecho por:"):
                    st.write("Rodrigo González López S4A")
        else:
            st.error("Recuerda que la semilla, la constanteA y la constanteC deben tener un número de dígitos pares e iguales y mayores, y las iteraciones deben ser mayores a 0.")
    except ValueError:
        st.error("Por favor, ingresa valores numéricos válidos para la semillam para las constantes y las iteraciones.")    