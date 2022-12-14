from django.shortcuts import render
from django.views import View

from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


# Create your views here.

class Detail_product(View):
    def get(self, request):
        return render(request, 'product/detail_product.html')


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_deleted=False)
