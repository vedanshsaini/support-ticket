from django.urls import path
from .views import SupportTicketListCreateView, SupportTicketDetailView, UserProfileDetailView,submit_ticket

urlpatterns = [
    path('tickets/', SupportTicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', SupportTicketDetailView.as_view(), name='ticket-detail'),
    path('user-profile/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('submit-ticket/', submit_ticket, name='submit_ticket'),
]
