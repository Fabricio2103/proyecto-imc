
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
