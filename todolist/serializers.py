from rest_framework import serializers
from .models import TodoItem

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username']

class TodoItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoItem
    fields = '__all__'