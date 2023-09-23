from django.urls import path
from my_test_app.views import BaseView

app_name = 'my_test_app'
urlpatterns = [
    path('', BaseView.as_view())
]