from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from eventex.core.models import Talk, Course
from eventex.registration.api.registration.serializers import RegistrationSerializer
from eventex.registration.models import Registration
from eventex.subscriptions.models import Subscription


class StudentViewSet(viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        estudantes = Registration.objects.all()
        serializer = RegistrationSerializer(estudantes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def select2(self, request):
        query = self.request.GET.get('term')
        if not query or query == '':
            return JsonResponse({"results": []})

        inscritos = Subscription.objects.filter(name__unaccent__icontains=query)

        results = {
            "results": [
                {"id": i.pk, "text": i.name} for i in inscritos
            ]
        }
        return JsonResponse(results)

    @action(detail=False, methods=["get"])
    def get_dados_student(self, request):
        student = Subscription.objects.filter(id=self.request.query_params.get('id')).first()

        if not student:
            return Response({"student": None})

        try:
            if not student.cpf:
                return Response({"cpf": None}, status=status.HTTP_404_NOT_FOUND)

            return Response(
                {"cpf": student.cpf, "phone": student.phone if student.phone else None},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["get"])
    def get_dados_talk(self, request):
        talk = Talk.objects.filter(id=self.request.query_params.get('id')).first()

        if not talk:
            return Response({"talk": None}, status=status.HTTP_404_NOT_FOUND)

        talk_speakers = [s.name for s in talk.speakers.all()]

        try:
            return Response(
                {"start": talk.start.strftime("%H:%M"), "speaker": talk_speakers}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["get"])
    def get_dados_course(self, request):
        course = Course.objects.filter(id=self.request.query_params.get('id')).first()

        if not course:
            Response({"course": None}, status=status.HTTP_404_NOT_FOUND)

        course_speakers = [s.name for s in course.speakers.all()]

        try:
            return Response(
                {"start": course.start.strftime("%H:%M"), "speaker": course_speakers}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
