from django.urls import path
from my_test_app.views import MainView, UserLoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

app_name = 'my_test_app'
urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout'),
]
