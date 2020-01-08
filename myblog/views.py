from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from myblog.models import Men, Women, Kid, Home_1, Home_2


# Create your views here.
def home(request):
#    home = {'name': Home.objects.all()}
#    return render(request, 'myblog/index.html', home)
	post1 = Home_1.objects.get(id=1)
	post2 = Home_1.objects.get(id=2)
	post3 = Home_1.objects.get(id=3)
	men = Home_2.objects.get(id=1)
	women = Home_2.objects.get(id=2)
	child = Home_2.objects.get(id=3)
	return render(request, 'myblog/index.html', {'post1': post1, 'post2': post2, 'post3': post3, 'men': men, 'women': women, 'child': child})

def mens(request):
    mens = {'name': Men.objects.all()}
    return render(request, 'myblog/mens.html', mens)


def womens(request):
    womens = {'name': Women.objects.all()}
    return render(request, 'myblog/womens.html', womens)


def kids(request):
    kids = {'name': Kid.objects.all()}
    return render(request, 'myblog/kids.html', kids)

