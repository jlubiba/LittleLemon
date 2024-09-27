from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.
@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def index(request):
    context = {}
    return render(request, "restaurant/index.html", context)

# class MenuItemView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticated]
    ordering_fields = ['BookingDate', 'no_of_guests']
    search_fields = ['name']
    
    def get_permissions(self):
        if self.action == 'retrieve' or  self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        
        return [permission() for permission in permission_classes]

class MenuItemView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price']
    search_fields = ['title']
    
    def get_permissions(self):
        if self.action != 'list' or self.action != 'retrieve':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]