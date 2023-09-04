"""
The views.py contains functions to perform codes based on various http requests
"""
from track.models import Unit
from track.serializers import UnitSerializer
from rest_framework import generics


class UnitView(generics.ListCreateAPIView):
    """
    The view handles the GET request for listing all 
    unit data and creation of unit.
    """
    serializer_class = UnitSerializer

    def get_queryset(self):
        """
        List all unit data from Unit model. 
        """
        phone_number = self.request.GET.get('phonenumber', '')
        unit_objs = Unit.objects.filter(worker__phone_number=phone_number)
        return unit_objs
