from rest_framework import serializers
from .models import User_Selection

class employeeserializer(serializers.ModelSerializer):

    class Meta:
        model=User_Selection
        #fields=('name','age')
        fields='__all__'