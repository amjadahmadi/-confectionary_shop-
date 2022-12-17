from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework import generics
from .models import Category, Stock
from .serializers import CategorySerializer, StockSerializer

from rest_framework import generics
from .models import Category, Stock, Products
from .serializers import CategorySerializer
from django.views.generic.detail import DetailView


# Create your views here.

class Detail_product(DetailView):
    model = Stock
    template_name = 'product/detail_product.html'
    queryset = Stock.objects.select_related('product')
    # def get_context_data(self, **kwargs):
    #     context = super(Detail_product, self).get_context_data(**kwargs)
    #     print(context['object']['product_name'])
    #     return context


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_deleted=False)


class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        if kwargs['category_id'] == 'all':
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(self.get_queryset().filter(category=kwargs['category_id']))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductList(generics.ListCreateAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        if kwargs['category_id'] == 'all':
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(self.get_queryset().filter(category=kwargs['category_id']))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
