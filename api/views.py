from rest_framework.generics import ListAPIView
from my_test_app.models import User
from api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)
