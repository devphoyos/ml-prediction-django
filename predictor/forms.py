# forms.py
from django import forms
from .models import ModelFile, ExcelFile

class FileUploadForm(forms.Form):
    excel_file = forms.FileField(label='Archivo Excel')  # Campo para cargar el archivo Excel
    model_file = forms.FileField(label='Modelo ML')
