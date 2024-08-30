from django.urls import path
from leads.views import  LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView #lead_list, lead_detail,lead_delete, lead_update, lead_create 

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
    path("<int:pk>/", LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/update", LeadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/delete", LeadDeleteView.as_view(), name="lead-delete"),
]
