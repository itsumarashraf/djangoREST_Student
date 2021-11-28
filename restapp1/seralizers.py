from rest_framework import fields, serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        # fields = "__all__"
        exclude=['id']