# from .models import *
#
#
# class ProductDetailSerializer(serializers.ModelSerializer):
#     """ Просмотр Заказа по ID """
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class ProductListSerializer(serializers.ModelSerializer):
#     """ Виводит все Закази """
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class ProductCreateSerializer(serializers.ModelSerializer):
#     """ Создание Поста """
#     date_joined = serializers.ReadOnlyField()