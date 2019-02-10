from rest_framework import serializers
from classes.models import Classroom

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'subject',
            'year',
            'teacher',
            ]


class ClassroomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'id',
            'teacher',
            'name',
            'subject',
            'year',
            ]

class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'subject',
            'year',
            ]