from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

