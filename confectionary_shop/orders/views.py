import json

from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrdersSerializer, OrderItemSerializer
from Cake_designing.serializers import CakeDesignSerializer


# Create your views here.


class Orders(View):
    def get(self, request):
        return render(request, 'orders/order_page.html')


class OrdersAPI(APIView):
    def post(self, request):
        order = json.loads(request.data['order'])
        print(request.data)
        serializer = OrdersSerializer(data=order)
        if serializer.is_valid():
            order = serializer.save()
        else:
            return Response(serializer.errors, status=401)
        order_items = json.loads(request.data['order_items'])
        cake_design = json.loads(request.data['cake_design'])
        list(map(lambda c: c.update({'order_id': order.id}), order_items))
        list(map(lambda z: z.update({'order_id': order.id, 'print_img': request.data.get('print' + z['id'], None),
                                     'sample_img': request.data.get('sample' + z['id'], None)}), cake_design))
        order_item_serializer = OrderItemSerializer(data=order_items, many=True)
        if order_item_serializer.is_valid():
            order_item_serializer.save()
        else:
            return Response(order_item_serializer.errors, status=401)
        if cake_design:
            cake_design_serializer = CakeDesignSerializer(data=cake_design, many=True)
            if cake_design_serializer.is_valid():
                cake_design_serializer.save()
            else:
                return Response(cake_design_serializer.errors, status=401)

        return Response(status=200)
