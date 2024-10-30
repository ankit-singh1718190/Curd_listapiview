from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView


# Create your views here.
class StudentModelViewSet(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreateModelViewSet(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  

class StudentRetriveCreateModelViewSet(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer  

class StudentUpdateModelViewSet(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer         

class StudentDestryModelViewSet(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer    

