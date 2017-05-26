from django.db import models

# Create your models here.

class DadosPessoais(models.Model):

	name = models.CharField(max_length = 200, verbose_name = 'Nome')
	address = models.CharField(max_length = 200, verbose_name = 'Endereço')
	city = models.CharField(max_length = 200, verbose_name = 'Cidade')
	zip_code = models.CharField(max_length = 50, verbose_name = 'Cep')
	phone = models.CharField(max_length = 20, verbose_name = 'Telefone')
	mobile = models.CharField(max_length = 20, verbose_name = 'Celular')

	about = models.TextField(max_length = 300, verbose_name = 'Sobre')
	birth_date = models.CharField(max_length = 100, default = '01 de janeiro de 1900', verbose_name = 'Data de nascimento')
	email  = models.EmailField(max_length = 100, verbose_name = 'email')

	knowledge = models.TextField(max_length = 300, verbose_name = 'Conhecimentos')
	github = models.CharField(max_length = 100, default = 'https://github.com/paulacusp', verbose_name = 'github')
	current_position = models.CharField(max_length = 50, verbose_name = 'Cargo atual')
	company = models.CharField(max_length = 50, verbose_name = 'Empresa')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Dados Pessoais'	
		verbose_name_plural = 'Dados Pessoais'