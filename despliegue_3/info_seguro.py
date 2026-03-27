from pypdf import PdfReader
import re

def buscador_palabras(search_word, path):
    """
    La siguiente función tiene como objectivo buscar una palabra 'search_word' y una vez encontrada
    si existe arrojará la linea dónde la encontró para su procesamiento,
    dado a que no necesariamente nuestra información estára en la palabra clave.
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

def extract_insurance_info(pdf_path):
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
    search_word1 = "C.P."
    search_word2 = "ASEGURADO"
    search_word3 = "AMIS"
    search_word4 = "PÓLIZA"
    search_word5 = "MONEDA"
    search_word6 = "PLAN"
    search_word7 = "No tiene avisos de cobro."
    #verificando que el archivo no esté en blanco
    resultado = buscador_palabras(search_word7, pdf_path)

    if resultado != 0:
        return None

    #procesando el nombre
    resultado = buscador_palabras(search_word1, pdf_path)
    nombre = lines[resultado]
    #procesando el monto a pagar
    resultado = buscador_palabras(search_word2, pdf_path)
    monto = lines[resultado - 2]
    #procesando el vehículo
    resultado = buscador_palabras(search_word3, pdf_path)
    split_parts = lines[resultado - 1].split("AMIS")
    if resultado == 0:
        auto_b = '***'
    else:
        auto_b = split_parts[0].strip()
        split_parts = auto_b.split(")")
        auto = split_parts[1].strip()
    #procesando póliza, endoso y fecha límite de pago
    resultado = buscador_palabras(search_word4, pdf_path)
    split_parts = lines[resultado - 1].split(" ")
    control = split_parts[6].split("CONTROL")
    poliza = control[1]
    endoso = split_parts[7]
    flimite = split_parts[8]
    #procesando serie y forma de pago
    resultado = buscador_palabras(search_word5, pdf_path)
    #print(lines[resultado])
    split_parts = lines[resultado].split("/")
    seriea = split_parts[1].lstrip()
    serie = split_parts[0]
    if seriea == '04':
        fpago = 'Trimestral'
    elif seriea == '02':
        fpago = 'Semestral'
    elif serie == '12':
        fpago = 'Mensual'
    elif serie == '01':
        fpago = 'contado'
    else:
        fpago = '*'
    #procesando Inicio y Fin de Vigencia
    resultado = buscador_palabras(search_word6, pdf_path)
    fini = lines[resultado].lstrip()
    ffin = lines[resultado + 1].lstrip()

    return{
        "Nombre": nombre,
        "Monto" : monto,
        "Auto" : auto,
        "Serie" : serie,
        "Seriea" : seriea,
        "Póliza" : poliza,
        "Endoso" : endoso,
        "Fecha Límite" : flimite,
        "Forma de pago" : fpago,
        "Inicio de Vigencia" : fini,
        "Fin de Vigencia" : ffin
    }


#cómo usar la función------
#pdf_path = r"C:\Users\lemon\mu_code\VSCODEprograms\streamlit\despliegue_3\Recibo.pdf"
#insurance_info = extract_insurance_info(pdf_path)
#print(insurance_info)


