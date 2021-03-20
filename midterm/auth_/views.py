from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LoginViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)



