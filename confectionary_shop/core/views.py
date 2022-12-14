from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'core/home.html', {'type': 'home'})
