import openpyxl
from openpyxl import Workbook

def calcular_imc(peso, altura):
    "Calcula el índice de masa corporal (IMC)."
    if altura <= 0:
        return None
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    "Clasificacion del Indice de Masa corporal"
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad ligera"
    elif 35 <= imc < 39.9:
        return "Obesidad"
    else:
        return "Obesidad mórbida"

def guardar_en_excel(datos, archivo='resultados_imc.xlsx'):
    "Guarda los datos en un archivo Excel utilizando openpyxl."
    try:
        wb = openpyxl.load_workbook(archivo)
    except FileNotFoundError:
        wb = Workbook()
        sheet = wb.active
        sheet.append(["Nombre", "Edad", "Genero", "Actividad Física", "Peso", "Altura", "IMC", "Clasificación"])

    sheet = wb.active
    sheet.append([datos['nombre'], datos['edad'], datos['genero'], datos['actividad'], datos['peso'], datos['altura'], datos['imc'], datos['clasificacion']])
    wb.save(archivo)