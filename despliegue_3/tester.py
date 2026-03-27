from pypdf import PdfReader
import re

def buscador_palabras(search_word, path):
    """
    La siguiente función tiene como objectivo buscar una palabra 'search_word' y 
    si no existe mandará una advertencia indicando que el archivo no pertenece a un 
    recibo pendiente de pago de Quálitas.
    """
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    lines = text.split("\n")
    contador = 0
    resultado = contador
    for line in lines:
        #print(line) ##para testing
        contador += 1
        if search_word in line:
            #print(f"la palabra '{search_word}' fue encontrada en la linea {contador}") # saber si encontró la palabra
            resultado = contador
            break
    if resultado == 0:
        #print(f"la palabra {search_word} no fue encontrada")
        t = 0
    return resultado

def extract_insurance_info_2(pdf_path):
    """
    La siguiente función tiene como objectivo definir nuestras palabras claves
    para la función buscador_palabras, si es que existé información en el pdf.
    después procesará la información para obtener los parametros del recibo
    pendiente de pago.
    """

    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    num_pages = len(reader.pages)
    lines = text.split("\n")
    search_word1 = "Quálitas"
    search_word2 = "AVISO DE COBRO"
    #verificando que el archivo no esté en blanco
    resultado = buscador_palabras(search_word1, pdf_path)

    if resultado == 0:
        return None
    resultado = buscador_palabras(search_word2, pdf_path)
    if resultado == 0:
        return None
    else: 
        return 1



#pdf_path = r"C:\Users\lemon\mu_code\VSCODEprograms\streamlit\despliegue_3\Recibo.pdf"
#insurance_info = extract_insurance_info(pdf_path)
#print(insurance_info)

