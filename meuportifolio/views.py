from django.shortcuts import render

# Create your views here.

def meuportifolio_exibir(request):
	return render(request, 'meuportifolio/meuportifolio_exibir.html', {})