from django.urls import path
from api.views import UserListAPIView, ProductListAPIView, StatisticsListAPIView

app_name = 'api'
urlpatterns = [
    path('user_list/', UserListAPIView.as_view(), name='user_list'),
    path('user_list/<int:product_id>', ProductListAPIView.as_view()),
    path('statistics/', StatisticsListAPIView.as_view(), name='statistics')
]
