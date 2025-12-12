Proyecto – TP Final Lenguajes

Este repositorio contiene el trabajo práctico que integra un análisis exploratorio de datos (EDA) realizado en Google Colab y una API desarrollada con FastAPI para consultar la información procesada.

Estructura del proyecto

/proyecto
│
├── Colab/# Notebook con el análisis
│
├── salida/# Carpeta generada por Colab
│     ├── datos_limpios.csv
│     ├── resumen.json
│
├── app.py/# API en FastAPI
│
└── README.md

__________________________________________

Cómo ejecutar el proyecto

Para que todo funcione correctamente, seguí estos pasos:

1) Abrir el Colab y correr todas las celdas (en orden)

El notebook realiza:

- Carga de datos

- Análisis exploratorio (EDA)

- Procesamiento y limpieza

- Generación de archivos finales

- Exportación de resultados

> IMPORTANTE: Ejecutar todas las celdas una por una hasta completar la creación de la carpeta salida/.

2) Colocar el archivo app.py junto a la carpeta salida/

La estructura correcta debe quedar así:

/mi_carpeta_de_trabajo
│
├── salida/
│     ├── ...archivos generados por Colab
│
└── app.py

3) Ejecutar la API

Abrí una terminal dentro de la carpeta donde está app.py y corré:

uvicorn app:app --reload

Luego ingresá en el navegador a:

http://127.0.0.1:8000/

Allí vas a encontrar:

- La descripción de la API

- Los endpoints disponibles

__________________________________________

🧪 Requisitos

Asegurate de tener instalado:

Python 3.10+

FastAPI

Uvicorn

Pandas


Instalación rápida:

pip install fastapi uvicorn pandas

__________________________________________

Autores y organización del trabajo

- Nicolás Torandell Ballesteros
- Gonzalo Redondo
- Marcos Giordano

El proyecto se realizó en tres partes:

1. Carga de datos, EDA inicial y procesamiento

2. Análisis central del proyecto

3. Exportación, construcción de la API y endpoints
