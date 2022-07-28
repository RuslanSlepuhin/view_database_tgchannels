from rest_framework import serializers

from .models import Telegramchannels


class GetAllMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telegramchannels
        fields = '__all__'