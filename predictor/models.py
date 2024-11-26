from django.db import models

# Create your models here.

class ModelFile(models.Model):
    model_file = models.FileField(upload_to='models/')  # Para almacenar el modelo ML
    
class ExcelFile(models.Model):
    excel_file = models.FileField(upload_to='uploads/')