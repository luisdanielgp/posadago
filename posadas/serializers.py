from rest_framework import serializers
from .models import Posada


class PosadaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posada
        fields = ('__all__')
