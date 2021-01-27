from rest_framework import serializers

from .models import Techniques

class TechniquesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Techniques
        fields = ('name', 'img')