"""
The views.py contains functions to perform codes based on various http requests
"""
from track.models import Unit
from track.serializers import UnitSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class UnitView(generics.ListCreateAPIView):
    """
    The view handles the GET and POST request for listing all 
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

    def post(self, request, format=None):
        """
        Create a new entry for unit in Unit model.
        """
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, 
                "message": "Unit created succesfully", 'data': serializer.data})
        return Response({"status": status.HTTP_400_BAD_REQUEST, 
            "message": "Unit creation failed", "data": serializer.errors})


class UnitDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    The view handles the GET, PUT and DELETE request for list a particular entry of 
    unit data, Edit a unit entry, Delete a unit entry.
    """
    serializer_class = UnitSerializer

    def get(self, request, pk, format=None):
        """
        List a unit entry from Unit model. 
        """
        details = None
        try:
            details = Unit.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 
                'message': "Unit detail not found"})
        serializer = UnitSerializer(details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit fields of a unit entry from Unit model. 
        """
        details = None
        try:
            details = Unit.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 
                'message': "Unit detail not found"})
        serializer = UnitSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 
                'message': "Unit details updated successfully", 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 
            'message': "Unit details updation failed", 'data': serializer.errors})

    def delete(self, request, pk, format=None):
        """
        Delete a unit entry from Unit model. 
        """
        try:
            if Unit.objects.filter(id=pk).exists():
                details = Unit.objects.get(id=pk)
                details.delete()
                return Response({'status': status.HTTP_200_OK, 
                    'message': "Unit detail deleted successfully"})
            else:
                return Response({'status': status.HTTP_404_NOT_FOUND, 
                    'message': "Unit detail not found"})
        except:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 
                'message': "Unit detail deletion failed"})
