from rest_framework import viewsets
from accounts.models import User
from accounts.seralizers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        self.queryset = User.objects.all()
        serializers_class = UserSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializers_class = UserSerializer(user)
        return Response(serializers_class.data)