from django.db.models.expressions import F
from rest_framework import viewsets
from .serializer import stack_serializer
from .models import stack
# Create your views here.

class stack_viewset(viewsets.ModelViewSet):
    queryset=stack.objects.all()
    serializer_class=stack_serializer

