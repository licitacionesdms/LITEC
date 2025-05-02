from django import forms
from .models import AlertaVencimiento, DispositivosMedicos

class AlertaVencimientoForm(forms.ModelForm):
    class Meta:
        model = AlertaVencimiento
        fields = ['registro_sanitario','fabricante','fecha_vencimiento']
        widgets = {
            'fecha_vencimiento':forms.DateInput(attrs={'type':'date'}),
        }

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = DispositivosMedicos
        fields = '__all__'  # Incluye todos los campos del modelo
        widgets = {

            'referencia_fabricante': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'referencia_lh': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'modelo': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'descripcion_espanol': forms.Textarea(attrs={
                'style': 'width: 200px; padding: 8px; border: 2px solid #000248; border-radius: 5px; height: 50px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
            'descripcion_ingles': forms.Textarea(attrs={
                'style': 'width: 200px; padding: 8px; border: 2px solid #000248; border-radius: 5px; height: 50px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
            'marca': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'fabricante': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'direccion_fabricante': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'nombre_registro_sanitario': forms.Textarea(attrs={
                'style': 'width: 200px; padding: 8px; border: 2px solid #000248; border-radius: 5px; height: 90px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
            'registro_sanitario': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'no_resolucion': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'fecha_aprobacion': forms.DateInput(attrs={
                'type': 'date', 
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'type': 'date', 
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
             'alerta_vencimiento': forms.DateInput(attrs={
                'type': 'date', 
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'expediente': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'radicado': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'modalidad': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'titular_registro_sanitario': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'importador': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'acondicionador': forms.TextInput(attrs={
                'style': 'width: 80%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'vida_util_anos': forms.NumberInput(attrs={
                'style': 'width: 50%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'vida_util_meses': forms.NumberInput(attrs={
                'style': 'width: 50%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'material_fabricacion': forms.Textarea(attrs={
                'style': 'width: 200px; padding: 8px; border: 2px solid #000248; border-radius: 5px; height: 50px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
            'clasificacion_riesgo': forms.TextInput(attrs={
                'style': 'width: 50%; padding: 8px; border: 2px solid #000248; border-radius: 5px;'
            }),
            'condiciones_almacenamiento': forms.Textarea(attrs={
                'style': 'width: 200px; padding: 8px; border: 2px solid #000248; border-radius: 5px; height: 50px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
            'tipo_dispositivo': forms.TextInput(attrs={
                'style': 'width: 200px; padding: 8px; border: 2px solid #000248; border-radius: 5px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
            'presentacion_comercial': forms.Textarea(attrs={
                'style': 'width: 250px; padding: 8px; border: 2px solid #000248; border-radius: 5px; font-family: Arial, sans-serif; font-size: 14px;'
            }),
        }

