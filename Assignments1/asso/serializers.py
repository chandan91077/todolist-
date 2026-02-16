from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'course']
    
    def validate_age(self, value):
        """
        Validate that age is greater than 5
        """
        if value <= 5:
            raise serializers.ValidationError("Age must be greater than 5")
        return value
