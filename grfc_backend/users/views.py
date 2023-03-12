# from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Subdivision
from .serializers import SubdivisionSerializer


class UserLoginView(LoginView):
    template_name = 'users/auth.html'
    success_url = reverse_lazy('users:home')


class HomeView(TemplateView):
    template_name = 'index.html'


class SubdivisionAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Возвращает запись по ключу'''
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class SubdivisionAPIList(generics.ListAPIView):
    '''Возвращает все записи из бд'''
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
