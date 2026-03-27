import streamlit as st
from PIL import Image
from pypdf import PdfReader
from info_seguro import extract_insurance_info
from tester import extract_insurance_info_2 
import pandas as pd
import re


def main():
    st.title("Recibo de cobro para Quálitas seguros.")

    archivo_doc = st.file_uploader("Subir Pdf para extracción de datos", type=["pdf"]) # Esto es para crear un botón de carga de archivos en la barra lateral que solo acepta archivos con las extensiones "pdf" y "docx" y guardar el archivo cargado en la variable "archivo_doc"
    if st.button("Obtener información"): # Esto es para crear un botón en la app con el texto "Procesar" y verificar si se ha presionado el botón
        if archivo_doc is not None:

            tester = extract_insurance_info_2(archivo_doc)
            print(tester)

            if tester == 1:

                info_seguro = extract_insurance_info(archivo_doc)


                st.write("**Resumen del recibo pendiente de pago:**")
                st.subheader(info_seguro['Nombre'])

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(label="Póliza", value=info_seguro["Póliza"])
                with col2:
                    st.metric(label="Monto a Pagar", value=f"${info_seguro['Monto']}")
                with col3:
                    st.metric(label="Fecha Límite de pago", value=info_seguro["Fecha Límite"])

                st.divider() # Una línea sutil para separar
                # 3. SECCIÓN MODIFICADA: Enfoque total en el Vehículo
                st.write("**🚗 Vehículo Asegurado:**") # Etiqueta en tamaño normal

                # Aquí mostramos SOLO el auto con letras GRANDES (Subheader)
                st.subheader(info_seguro['Auto'])
                    

                # 1. Creamos el texto limpio (sin llaves ni comillas)
                mensaje_limpio = f"""Póliza: {info_seguro['Póliza']}

Monto a pagar: {info_seguro['Monto']}
Vehículo: {info_seguro['Auto']}
Fecha Límite de pago: {info_seguro['Fecha Límite']}"""

                # 2. Lo mostramos en un bloque de código
                # Usamos language=None para que no intente resaltar colores de programación
                st.write("Aquí abajo puedes copiar la información de tu póliza:")
                st.code(mensaje_limpio, language=None)

            else:
                st.error("Archivo no identificado, Por favor ingrese un aviso de cobro de Quálitas")
                


if __name__ == '__main__':
    main()


#remover antes del despliegue
#cd C:\Users\lemon\mu_code\VSCODEprograms\streamlit\despliegue_3
#streamlit run app_extraer_info.py