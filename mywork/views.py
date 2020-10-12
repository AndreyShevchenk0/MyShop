# from rest_framework import generics
# from mywork.serializers import ProductDetailSerializer, ProductListSerializer, ProductCreateSerializer
# from mywork.models import Product
# from mywork.permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
#
#
# class ProductCreateView(generics.CreateAPIView,):
#     """ Создание Записи """
#     serializer_class = ProductDetailSerializer
#
#
# class ProductListView(generics.ListAPIView):
#     """ Просмотр всех записей   """
#     serializer_class = ProductListSerializer
#     queryset = Product.objects.all()
#     permission_classes = (IsAuthenticated,)
#
# class ProductDetailView(generics. RetrieveUpdateDestroyAPIView):
#     """ Просмотр конкретних записей, редактирование и удаление! """
#     serializer_class = ProductDetailSerializer
#     queryset = Product.objects.all()
#     permission_classes = (IsOwnerOrReadOnly,)
