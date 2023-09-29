from django.shortcuts import render
from rest_framework import generics

from .serializers import MenuSerializer
from .models import Menu

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()