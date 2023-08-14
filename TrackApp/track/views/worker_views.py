"""
The views.py contains functions to perform codes based on various http requests
"""
from track.models import Worker
from track.serializers import WorkerSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class WorkView(generics.ListCreateAPIView):
    """
    The view handles the GET and POST request for listing all 
    worker data and creation of worker.
    """
    serializer_class = WorkerSerializer

    def get_queryset(self):
        """
        List all worker data from Worker model. 
        """
        worker_objs = Worker.objects.all()
        return worker_objs

    def post(self, request, format=None):
        """
        Create a new entry for worker in Worker model.
        """
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, 
                "message": "Worker created succesfully", 'data': serializer.data})
        return Response({"status": status.HTTP_400_BAD_REQUEST, 
            "message": "Worker creation failed", "data": serializer.errors})


class WorkerDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    The view handles the GET, PUT and DELETE request for list a particular entry of 
    worker data, Edit a worker entry, Delete a worker entry.
    """
    serializer_class = WorkerSerializer

    def get(self, request, pk, format=None):
        """
        List a worker entry from Worker model. 
        """
        details = None
        try:
            details = Worker.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 
                'message': "Worker detail not found"})
        serializer = WorkerSerializer(details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit fields of a worker entry from Worker model. 
        """
        details = None
        try:
            details = Worker.objects.get(id=pk)
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND, 
                'message': "Worker detail not found"})
        serializer = WorkerSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 
                'message': "Worker details updated successfully", 'data': serializer.data})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 
            'message': "Worker details updation failed", 'data': serializer.errors})

    def delete(self, request, pk, format=None):
        """
        Delete a worker entry from Worker model. 
        """
        try:
            if Worker.objects.filter(id=pk).exists():
                details = Worker.objects.get(id=pk)
                details.delete()
                return Response({'status': status.HTTP_200_OK, 
                    'message': "Worker detail deleted successfully"})
            else:
                return Response({'status': status.HTTP_404_NOT_FOUND, 
                    'message': "Worker detail not found"})
        except:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 
                'message': "Worker detail deletion failed"})
