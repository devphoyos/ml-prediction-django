# Aplicación de Predicción con Modelo ML

Este proyecto es una aplicación web desarrollada en **Django** que permite cargar un modelo de **Machine Learning** preentrenado y un archivo de datos en formato **Excel**. La aplicación hace predicciones basadas en el modelo cargado y muestra los resultados en una tabla en la interfaz web.

## Funcionalidades

1. **Carga del modelo ML**: Permite cargar un archivo de modelo preentrenado en formato `.pkl`.
2. **Carga del archivo Excel**: Permite cargar un archivo Excel con los datos necesarios para hacer las predicciones.
3. **Predicción**: Realiza predicciones utilizando el modelo cargado y muestra los resultados en una tabla en la misma página web.
4. **Interfaz de usuario**: La interfaz es sencilla y permite al usuario cargar ambos archivos a través de un formulario.

## Tecnólogías usadas

- Python 3.13.0
- Django 5.1.3

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instalar las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```
   Esto arrancará el servidor en http://127.0.0.1:8000/.

### Example_Files

Este directorio contiene unos archivos para relizar pruebas, el modelo predice el precio promedio de las casas en un bloque residencial en California basándote en características como el ingreso promedio, la población y la ubicación geográfica.
