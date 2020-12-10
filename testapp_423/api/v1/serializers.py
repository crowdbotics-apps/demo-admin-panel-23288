from rest_framework import serializers
from testapp_423.models import Aaa


class AaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aaa
        fields = "__all__"
