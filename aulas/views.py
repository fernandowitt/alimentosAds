from django.shortcuts import render, redirect
from .models import Aula
from .forms import FormularioAula

#usar login required aqui
def criarNovaAula(request):
	formAula = FormularioAula()
	if request.method == "POST":
		aulaForm = FormularioAula(request.POST)
		if aulaForm.is_valid():
			aula = aulaForm.save(commit = False)
			aula.autor = request.user
			aula.video = "https://www.youtube.com/embed/"+aula.video
			aula.save()
			return redirect('aulasList')
	return render(request, 'HTML/aula.html', {'formAula':formAula})

def aulasList(request):
	aulas = Aula.objects.all()
	return render(request, 'HTML/inicio.html', {'aulas':aulas})

def aula(request, pk):
	aula = Aula.objects.get(pk = pk)
	return render(request, 'HTML/aulaDetail.html', {'aula':aula})

