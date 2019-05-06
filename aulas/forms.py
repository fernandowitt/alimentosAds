from django import forms
from .models import Aula

class FormularioAula(forms.ModelForm):
	class Meta:
		model = Aula
		fields = ('titulo', 'assuntos', 'conteudo', 'video', 'ativo')


