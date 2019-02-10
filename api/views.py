from django.shortcuts import render
from classes.models import Classroom
# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    ClassroomListSerializer,
    ClassroomDetailSerializer,
    ClassroomCreateUpdateSerializer,
)
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .permissions import IsTeacher

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    permission_classes = [AllowAny]

class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'

class ClassroomCreateView(CreateAPIView):
    serializer_class = ClassroomCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'class_id'