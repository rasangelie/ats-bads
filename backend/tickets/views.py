from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TicketSerializer
from .models import Ticket



# class TicketListCreate(ListCreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

class TicketListCreate(GenericAPIView):
    """
    Creating Ticket 
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]


    def get(self, request: Request) -> Response:
        ticket_list = self.get_queryset()
        serializer = self.serializer_class(ticket_list, many=True)

        return Response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TicketUpdateView(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
