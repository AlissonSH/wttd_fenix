from rest_framework import serializers
from eventex.registration.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    student_paid = serializers.ReadOnlyField(source='student.paid')

    class Meta:
        model = Registration
        fields = ['student', 'student_name', 'cpf', 'phone', 'student_paid']
