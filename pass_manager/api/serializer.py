from rest_framework import serializers
from .models import PassSite

class PassSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassSite

        fields = (
            '__all__'
        )
