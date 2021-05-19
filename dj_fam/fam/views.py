from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets, mixins
from .models import Human
from .serializers import HumanSerializer
import json


# Create your views here.


def home(request):
    return HttpResponse("Homescreen says: Hello world!")


class Fam(viewsets.ModelViewSet, mixins.CreateModelMixin):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()

    def create(self, request, serializer_class=serializer_class, queryset=queryset):
        human = serializer_class(data=request.data)
        if human.is_valid():
            human.save()
            return JsonResponse(human.data)
        else:
            return JsonResponse(human.errors)

"""
    @csrf_exempt
    def add_human(request):
        if request.method == 'POST':
            human = HumanSerializer(data=json.loads(request.body))
            if human.is_valid():
                human.save()
                return JsonResponse(human.data)
            else:  
                return JsonResponse(human.errors)

        if request.method == 'GET':
            return HttpResponse("Post a new human to this address.")
"""

"""
    def get_human(request):
        try:
            getter = Human.objects.get(name=request.GET['name'])
            human = HumanSerializer(getter)
            return JsonResponse(human.data)
        except MultiValueDictKeyError:
            return HttpResponse("append to the URL: '?name=______' to retrieve it from the DB.")
"""

"""
    def get_all(request):
        all = {}
        for human in Human.objects.all():
            all[HumanSerializer(human).data['id']] = HumanSerializer(human).data
        return JsonResponse(all)
"""