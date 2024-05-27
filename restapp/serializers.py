from rest_framework import serializers
from .models import restapi,CustomUser

class restserializer(serializers.ModelSerializer):
    class Meta:
        model = restapi
        fields = '__all__'


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

