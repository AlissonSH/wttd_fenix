from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from eventex.registration.models import Registration
from eventex.subscriptions.models import Subscription


class StudentViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=["get"])
    def select2(self, request):

        query = self.request.GET.get('term')
        print(query)
        if not query or query == '':
            return JsonResponse({"results": []})

        inscritos = Subscription.objects.filter(name__icontains=query)

        results = {
            "results": [
                {"id": i.pk, "text": i.name} for i in inscritos
            ]
        }

        return JsonResponse(results)
