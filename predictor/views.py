from django.shortcuts import render
import pandas as pd
import pickle
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def save_file(file, filename):
    """Guarda un archivo temporalmente y retorna su ruta."""
    if not file:
        return None
    file_path = default_storage.save(filename, ContentFile(file.read()))
    return file_path


def load_model(file_path):
    """Carga un modelo desde un archivo."""
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise ValueError(f"Error al cargar el modelo: {e}")


def validate_excel_columns(data, required_columns):
    """Valida que el archivo Excel tenga las columnas requeridas."""
    if not all(col in data.columns for col in required_columns):
        missing_cols = ', '.join(required_columns)
        raise ValueError(f"El archivo Excel debe contener las columnas: {missing_cols}")


def make_predictions(model, data, required_columns):
    """Hace las predicciones con el modelo."""
    features = data[required_columns]
    predictions = model.predict(features)
    data['Prediction'] = [round(pred, 2) for pred in predictions]
    return data


def upload_and_predict(request):
    context = {}

    if request.method == 'POST':
        # Subir y cargar modelo
        model_file = request.FILES.get('model')
        model_path = save_file(model_file, 'temp_model.pkl')

        if not model_path:
            context['error'] = "Por favor, suba un archivo de modelo."
            return render(request, 'predictor/upload.html', context)

        try:
            model = load_model(model_path)
        except ValueError as e:
            context['error'] = str(e)
            return render(request, 'predictor/upload.html', context)

        # Subir archivo Excel
        excel_file = request.FILES.get('file')
        excel_path = save_file(excel_file, 'temp.xlsx')

        if not excel_path:
            context['error'] = "Por favor, suba un archivo Excel."
            return render(request, 'predictor/upload.html', context)

        try:
            # Leer el archivo Excel
            data = pd.read_excel(excel_path)

            # Verificar columnas requeridas
            required_columns = model.feature_names_in_
            validate_excel_columns(data, required_columns)

            # Hacer predicciones
            data = make_predictions(model, data, required_columns)

            # Preparar datos para la tabla
            context['table'] = data.to_html(index=False, 
                                 header=True, 
                                 classes='table-auto min-w-full border-collapse border border-slate-400 text-center', 
                                 border=1)

        except ValueError as e:
            context['error'] = str(e)
        except Exception as e:
            context['error'] = f"Error al procesar el archivo Excel o al predecir: {e}"

        finally:
            # Eliminar archivos temporales
            default_storage.delete(model_path)
            default_storage.delete(excel_path)

    return render(request, 'predictor/upload.html', context)