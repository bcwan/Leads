from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset (helps us with CRUD API, and have default routers)
class LeadViewSet(viewsets.ModelViewSet):
  # get all the objects of Leads
  queryset = Lead.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = LeadSerializer
