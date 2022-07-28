
from rest_framework import viewsets
from .models import Telegramchannels
from .serializers import GetAllMessagesSerializer


class GetAllMessagesView(viewsets.ModelViewSet):
    queryset = Telegramchannels.objects.all().order_by('-time_of_public')
    serializer_class = GetAllMessagesSerializer
