from django.db import models
from rest_framework import serializers
from .models import stack


class stack_serializer(serializers.ModelSerializer):
        class Meta:
            model=stack
            fields='__all__'
