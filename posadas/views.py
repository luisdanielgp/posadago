from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Posada
from django.http import Http404
from .serializers import PosadaModelSerializer


class ListarPosadas(APIView):
    '''
    Este endpoint trae todas las posadas
    '''

    def get(self, request):
        posadas = Posada.objects.all()
        serializer = PosadaModelSerializer(posadas, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PosadaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PosadaIndividual(APIView):

    def _get_posada(self, id):
        try:
            posada = Posada.objects.get(pk=id)
            return posada
        except Posada.DoesNotExist:
            raise Http404

    def get(self, request, id):
        posada = get_object_or_404(Posada, pk=id)
        serializer = PosadaModelSerializer(posada)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        posada = self._get_posada(id)
        serializer = PosadaModelSerializer(posada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        posada = self._get_posada(id)
        serializer = PosadaModelSerializer(
            posada, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        posada = self._get_artist(id)
        posada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
