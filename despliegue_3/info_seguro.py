from pypdf import PdfReader
import re

def extract_insurance_info(path):
    """
    La siguiente función va a leer un PDF y separarlo por lineas
    Con un Diccionario para las palabras clave que por defecto no van a tener nada
    Vamos a hacer un ciclo for para navegar por todas las lineas del texto
    Dentro de ese ciclo for va a ver otro ciclo for donde vamos a recorrer todo el diccionario de posiciones
    Si el archivo no es una póliza de Chubb, entonces va a regresar None
    En ese ciclo vamos a buscar si existe alguna de nuestras palabra clave y de existir, 
    vamos a tomar el número de linea dónde está la palabra

    En la siguiente parte vamos a procesar las lineas para extraer nuestra información deseada: Nombre, Póliza, Monto, Fecha límite de pago

    y finalmente regresamos la información
    """

    reader = PdfReader(path)
    number_of_pages = len(reader.pages)  #para que usamos esto?
    page = reader.pages[0]
    text = page.extract_text()
    lines = text.split("\n")


    posiciones_de_palabras = { 
        "C.P." : None, 
        "ASEGURADO": None,   # la ini y fin vigencia también está aquí
        "AMIS": None,
        "PÓLIZA": None,
        "MONEDA": None,
        "PLAN": None,
        "No tiene avisos de cobro.": None
        }


    for line_number, line in enumerate(lines):
        #print(line)
        for palabra, posicion in posiciones_de_palabras.items():
            if palabra in line and posiciones_de_palabras[palabra] is None:
                posiciones_de_palabras[palabra] = line_number

    ###Condicional Qualitas Seguros 

    #if posiciones_de_palabras["No tiene avisos de cobro."] == None:
        #return None

    ####Nombre
    nombre = lines[posiciones_de_palabras["C.P."] + 1]

    ###Monto
    monto = lines[posiciones_de_palabras["ASEGURADO"] - 1]

    #procesando el vehículo
    existencia_vehiculo = lines[posiciones_de_palabras["AMIS"]]
    separar_para_auto = lines[posiciones_de_palabras["AMIS"]].split("AMIS")
    if existencia_vehiculo == None:
        auto = '***'
    else:
        cadena_auto_original = separar_para_auto[0].strip()
        partes = cadena_auto_original.split(")")
        auto = partes[1].strip()

    ###Serie
    recibos_cadena_posicion = posiciones_de_palabras["MONEDA"] + 1
    separar_recibos_cadena = lines[recibos_cadena_posicion].split("/")
    total_recibos = separar_recibos_cadena[1].lstrip()
    recibo_actual = separar_recibos_cadena[0]

    if total_recibos == '04':
        formapago = 'Trimestral'
    elif total_recibos == '02':
        formapago = 'Semestral'
    elif total_recibos == '12':
        formapago = 'Mensual'
    elif total_recibos == '01':
        formapago = 'contado'
    else:
        formapago = '*'

    #procesando póliza, endoso y fecha límite de pago
    poliza_endoso_vencimiento_posicion = posiciones_de_palabras["PÓLIZA"]
    separar_datos_cadena = lines[poliza_endoso_vencimiento_posicion].split(" ")
    separar_dato_poliza = separar_datos_cadena[6].split("CONTROL")

    poliza = separar_dato_poliza[1]
    endoso = separar_datos_cadena[7]
    flimite = separar_datos_cadena[8]

    #procesando Inicio y Fin de Vigencia
    ancla_vigencia_posicion = posiciones_de_palabras["PLAN"]
    fecha_ini_vigencia = lines[ancla_vigencia_posicion + 1].lstrip()
    fecha_fin_vigencia = lines[ancla_vigencia_posicion + 2].lstrip()

    print("termino el debug")

    return{
        "Nombre": nombre,
        "Monto" : monto,
        "Auto" : auto,
        "Serie" : recibo_actual,
        "Seriea" : total_recibos,
        "Póliza" : poliza,
        "Endoso" : endoso,
        "Fecha Límite" : flimite,
        "Forma de pago" : formapago,
        "Inicio de Vigencia" : fecha_ini_vigencia,
        "Fin de Vigencia" : fecha_fin_vigencia
    }




