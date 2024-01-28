from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response 

from django.http import JsonResponse

def index(request):
    return JsonResponse({'status': 'success'})
