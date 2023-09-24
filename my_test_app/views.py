from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from my_test_app.forms import UserLoginForm


class MainView(TemplateView):
    template_name = 'main.html'


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm


class UserProductsView(TemplateView):
    template_name = 'user_products.html'


class StatisticsView(TemplateView):
    template_name = 'statistics.html'
