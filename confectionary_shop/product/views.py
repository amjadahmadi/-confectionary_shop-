from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework import generics
from .models import Category, Stock
from .serializers import CategorySerializer, StockSerializer


# Create your views here.

class Detail_product(View):
    def get(self, request):
        return render(request, 'product/detail_product.html')


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_deleted=False)


class ProductList(generics.ListCreateAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(category=kwargs['category_id']))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
