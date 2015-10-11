from django.shortcuts import render
from src.models import Home
from src.models import About
from src.models import Corporate
from src.models import Interior
from src.models import Building
from src.models import Icon
from src.models import Modular
from src.models import Construction
from src.models import Fabrication


# Create your views here.
def index(request):
	return render(request, 'index.html')
def r(request):
	return render(request, 'r.html')
def b(request):
	return render(request, 'b.html')
def f(request):
	return render(request, 'f.html')
def m(request):
	return render(request, 'm.html')
def corp(request):
	return render(request, 'corp.html')
def const(request):
	return render(request, 'const.html')
