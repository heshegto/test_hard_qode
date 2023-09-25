from rest_framework.generics import ListAPIView
from my_test_app.models import Accesses, Product
from api.serializers import ProductSerializer, ProductStatisticsSerializer
from rest_framework.permissions import IsAuthenticated


# Задание 2.1
class UserListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        accesses_to_products = Accesses.objects.filter(user=self.request.user).values('accesses')
        return Product.objects.filter(pk__in=accesses_to_products)


# Задание 2.2
class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if Accesses.objects.filter(user=self.request.user, accesses=self.kwargs.get('product_id')):
            return Product.objects.filter(id=self.kwargs.get('product_id'))
        else:
            return None


# Задание 2.3
class StatisticsListAPIView(ListAPIView):
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        return Product.objects.all()
