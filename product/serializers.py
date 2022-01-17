from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Класс который переводит данные в json формат
    """
    class Meta:
        model = Product
        exclude = ('created_at',)
        # exclude = ('created_at', )
        # fields = ('id', 'title', 'price', 'status', 'description', 'image')
        # fields = "__all__"
        # fields = ("title", "status", "description", "price", "image", "total_sum")


class ProductCreateSerializer(serializers.ModelSerializer):
    """
    Класс который переводит данные в json формат
    """
    class Meta:
        model = Product
        fields = ('title', 'image', 'price', 'description')

