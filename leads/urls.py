from django.urls import path
from .views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView
    )

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('detail/<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead_update'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead_delete'),
]