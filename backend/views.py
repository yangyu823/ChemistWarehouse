from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
from datetime import datetime
from backend.Price_get.get_data import check_data
from backend.Price_get.update_data import get_list
from backend.Price_get.update_data import update_price
from backend.models import Backend
from backend.serializers import BackendSerializer
from rest_framework import generics


# Create your views here.

class BackendListCreate(generics.ListCreateAPIView):
    queryset = Backend.objects.all()
    serializer_class = BackendSerializer


@api_view(["POST"])
def TestPost(test_data):
    try:
        result = str(json.loads(test_data.body))
        # print(url)
        # return JsonResponse(result, safe=False)
        return Response(result)
    except ValueError as e:
        return Response(status.HTTP_400_BAD_REQUEST)

        # return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def NewAPI(data):
    try:
        url = json.loads(data.body)
        result = check_data(url)
        # print(url)
        # print(result)
        return JsonResponse(result, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def TestGet(request):
    try:
        result = "Hello world"
        return Response(result)
    except ValueError as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def Time(request):
    try:
        return Response(datetime.now())
    except ValueError as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def Update(request):
    try:
        result = get_list()
        update_price(result)
        if not result:
            return JsonResponse("All data up to date", safe=False)
        else:
            return JsonResponse(result, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
