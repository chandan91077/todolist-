from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=False, methods=['get', 'post'])
    def create_hardcoded_student(self, request):
        """
        Creates a student with hardcoded data from the code itself
        """
        # Hardcoded student data
        student_data = {
            'name': 'John Doe',
            'age': 20,
            'course': 'Computer Science'
        }
        
        if request.method == 'GET':
            # Show what will be created
            return Response({
                'message': 'This will create a student with the following hardcoded data:',
                'data': student_data
            })
        
        # Create student using the hardcoded data
        student = Student.objects.create(**student_data)
        serializer = self.get_serializer(student)
        
        return Response({
            'message': 'Student created with hardcoded data',
            'student': serializer.data
        })
