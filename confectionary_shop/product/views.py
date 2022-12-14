from django.shortcuts import render
from django.views import View


# Create your views here.

class Detail_product(View):
    def get(self, request):
        return render(request, 'product/detail_product.html')
