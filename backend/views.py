from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from backend.Price_get.get_data import check_data


# Create your views here.

@api_view(["POST"])
def TestAPI(test_data):
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
        print(url)
        print(result)
        return JsonResponse(result, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def test(request):
    try:
        result = "Hello world"
        return Response(result)
    except ValueError as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
