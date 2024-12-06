# Proyecto IMC (Índice de Masa Corporal)

El Índice de Masa Corporal (IMC) es un valor que se utiliza para evaluar si una persona tiene un peso adecuado en relación con su altura. Es una herramienta clave en el ámbito de la salud, utilizada para identificar posibles riesgos asociados al sobrepeso, obesidad o bajo peso. El IMC se calcula dividiendo el peso en kilogramos por el cuadrado de la altura en metros.

## Características del Proyecto

Este proyecto cuenta con las siguientes funcionalidades:

- **Interfaz Gráfica Intuitiva:**  
  Utiliza la biblioteca Tkinter para ofrecer una experiencia visual amigable y fácil de usar. Desde la interfaz, el usuario puede:  
  - Ingresar datos como peso y altura para calcular su IMC.  
  - Ver resultados claros y comprensibles con mensajes personalizados que indican el estado del IMC (bajo peso, normal, sobrepeso, etc.).

- **Sistema de Almacenamiento de Datos:**  
  - Los datos ingresados por los usuarios, junto con los resultados del IMC, se registran automáticamente en un archivo Excel.  
  - Este archivo permite guardar un historial para análisis posterior o para seguimiento del estado de salud.  
  - Se utiliza la biblioteca `openpyxl` para garantizar un manejo eficiente y confiable de los datos.

- **Generación de Archivo Ejecutable:**  
  - El proyecto incluye la capacidad de generar un archivo ejecutable, lo que permite que cualquier persona pueda usarlo sin necesidad de tener Python instalado.  
  - Este ejecutable es portable y facilita el acceso a un público más amplio.


