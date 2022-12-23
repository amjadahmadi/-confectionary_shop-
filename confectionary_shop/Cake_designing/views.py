from django.shortcuts import render
from django.views import View
from .forms import CakeDesigningForm


# Create your views here.

class CakeDesigning(View):
    def get(self, request):
        f = CakeDesigningForm()
        print(f)
        return render(request, 'Cake_designing/cake_design.html', {'form': f})
