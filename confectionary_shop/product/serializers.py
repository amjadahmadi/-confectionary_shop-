from .models import Category, Stock, Discount, Products, Discount_Code
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
        dis = obj.get_discount()
        if dis:
            obj.after_discount = obj._after_discount(dis['amount'], dis['percent'])
        return dis

    # def get_dis(self, obj: Stock):
    #     _discount = obj.get_discount
    #     print(_discount)
    #     return _discount
# class DiscountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Discount
#         fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount_Code
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    after_discount = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = Stock
        fields = '__all__'

    def get_after_discount(self, obj: Stock):
        dis = obj.get_discount()
        if dis:
            return obj._after_discount(dis['amount'], dis['percent'])
        return None

    # def get_dis(self, obj: Stock):
    #     _discount = obj.get_discount
    #     print(_discount)
    #     return _discount
