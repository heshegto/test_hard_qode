from rest_framework.generics import ListAPIView
from my_test_app.models import User, Accesses, Product
from api.serializers import UserSerializer, AccessesSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated


# Задание 2.1
class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)


# Задание 2.2
class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if Accesses.objects.filter(user=self.request.user, accesses=self.kwargs.get('product_id')):
            return Product.objects.filter(id=self.kwargs.get('product_id'))
        else:
            return None

