from .models import Category, Stock, Discount, Products
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = Stock
        fields = '__all__'

    def get_discount(self, obj: Stock):
        dis = obj.get_product()
        if dis:
            obj.after_discount = obj._after_discount(dis['amount'], dis['percent'])
        return dis

    # def get_dis(self, obj: Stock):
    #     _discount = obj.get_discount
    #     print(_discount)
    #     return _discount
