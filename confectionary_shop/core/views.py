from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import activate


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'core/home.html', {'type': 'home'})


class ChangeLanguage(View):
    def get(self, request):
        activate(request.GET.get('lang'))
        return redirect(request.GET.get('next'))
