from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import sys
sys.path.append("..")
from core.models import Tag

from . import serializers

# Create your views here.
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
  """Manage tags in the database"""
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = Tag.objects.all()
  serializer_class = serializers.TagSerializer

  def get_queryset(self):
    """Return objects for the current authenticated user only"""
    return self.queryset.filter(user=self.request.user).order_by('-name')
