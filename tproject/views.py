from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Image, Level
from .serializers import ImageSerializer, LevelSerializer, CustomUserSerializer
from .permissions import ImagePermission


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, ImagePermission]

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        level = self.request.user.level
        if not level:
            level = Level.objects.get(name='Basic')
        serializer.save(owner=self.request.user, level=level)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAdminUser]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
