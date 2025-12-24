from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ServiceRequestViewSet(ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_request = serializer.save()
        #send confirmation email logic can be added here
        return Response({
            "message": "Service request created successfully"}
            , status=status.HTTP_201_CREATED)