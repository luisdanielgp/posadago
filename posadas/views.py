from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Posada
from django.http import Http404

class ListarPosadas(APIView):

    def get (self, request):
        