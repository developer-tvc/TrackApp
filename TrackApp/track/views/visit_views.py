"""
The views.py contains functions to perform codes based on various http requests
"""
from track.models import Visit, Unit
from track.serializers import VisitSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class VisitView(generics.ListCreateAPIView):
    """
    The view handles the GET and POST request for listing all 
    visit data and creation of visit entry.
    """
    serializer_class = VisitSerializer

    def get_queryset(self):
        """
        List all visit data from Visit model. 
        """
        visit_objs = Visit.objects.all()
        return visit_objs

    def post(self, request, format=None):
        """
        Create a new visit entry in Visit model.
        """
        unit_id= request.data.get('unit')
        phone_number = self.request.query_params.get('phonenumber', '')
        worker_units = Unit.objects.filter(worker__phone_number=phone_number).values_list('id', flat=True)
        unit_id_list = list(worker_units)
        if unit_id in unit_id_list:
            serializer = VisitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": status.HTTP_201_CREATED, 
                    "message": "Visit entry created succesfully", 'data': serializer.data})
            return Response({"status": status.HTTP_400_BAD_REQUEST, 
                "message": "Visit entry creation failed", "data": serializer.errors})
        else:
            return Response({"status": status.HTTP_400_BAD_REQUEST, 
                "message": "Worker does not associated to the unit"})
