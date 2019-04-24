from django.db import models
from django.utils import timezone

# Create your models here.


class Aulas(models.Model):
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	titulo = models.CharField(max_length = 80)
	ASSUNTOS = (
		('ECA', 'ENTENDENDO A CONTAMINAÇÃO DOS ALIMENTOS'), 
		('AMA', 'AMBIENTE DE MANIPULAÇÃO E CUIDADOS COM ÁGUA'),
		('MLV', 'MANUSEIO DO LIXO E CONTROLE DE VETORES E PRAGAS'),
		('HIG', 'HIGIENIZAÇÃO'),
		('MEV', 'MANIPULADORES E VISITANTES'),
		('EDM', 'ETAPAS DA MANIPULAÇÃO'),
		('DOC', 'DOCUMENTAÇÃO'),

		)
	assuntos = models.CharField(max_length = 2, choices = ASSUNTOS, default='ECA')
	conteudo = models.TextField()
	video = models.CharField(max_length = 500)
	ativo = models.BooleanField(default=True)


class Comentario(models.Model):
	#criar classe aluno
	aula = models.ForeignKey(Aulas, on_delete=models.CASCADE)
	comentario = models.TextField()

	def published_date(self):
		published_date = timezone.now()
		self.save()


