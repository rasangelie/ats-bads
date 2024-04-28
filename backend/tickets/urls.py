from django.urls import path
from .views import TicketListCreate, TicketUpdateView

urlpatterns = [
    path('tickets/', TicketListCreate.as_view(), name='tickets-list-create'),
    path('update-ticket/<uuid:pk>/', TicketUpdateView.as_view(), name='ticket-update'),

]