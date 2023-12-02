from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoItem
    #fields = '__all__'
    fields = ['id', 'title', 'created_at', 'author']