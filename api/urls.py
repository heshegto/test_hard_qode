from django.urls import path
from api.views import UserListAPIView

app_name = 'api'
urlpatterns = [
    path('user_list/', UserListAPIView.as_view(), name='user_list'),
]
