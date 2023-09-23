from django.urls import path
from my_test_app.views import MainView

app_name = 'my_test_app'
urlpatterns = [
    path('', MainView.as_view(), name='main')
]
