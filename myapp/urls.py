from django.urls import path
from .views import StudentModelViewSet,StudentDestryModelViewSet,StudentCreateModelViewSet,StudentRetriveCreateModelViewSet,StudentUpdateModelViewSet
urlpatterns = [
    path('get/', StudentModelViewSet.as_view(), name='student-list'),
    path('<int:pk>/', StudentDestryModelViewSet.as_view(), name='student-dserty'),
    path('c/', StudentCreateModelViewSet.as_view(), name='student-create'),
    path('get/<int:pk>/',StudentRetriveCreateModelViewSet.as_view(), name='student-retrive'),
    path('update/<int:pk>/',StudentUpdateModelViewSet.as_view(), name='student-update'),
]
