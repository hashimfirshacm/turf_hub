from django.shortcuts import render

# Create your views here.
from turf_management.models import Turf

from turf_management.serializer import TurfSerializers

from rest_framework.views import APIView

from rest_framework.response import Response

class TurfListCreateView(APIView):

    def get(self,request):

        qs = Turf.objects.all()

        serializer_instance = TurfSerializers(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = TurfSerializers(data = form_data)

        if serializer_instance.is_valid():

            #cleaned_data = serializer_instance.validated_data
            #Turf.object.create(**cleaned_data)

            serializer_instance.save()#create

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
            

class TurfRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk = None):

        qs = Turf.objects.filter(id = pk)

        serializer_instance = TurfSerializers(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk = None):
        turf_object = Turf.objects.get(id=pk)

        form_data = request.data

        serializer_instance = TurfSerializers(data=form_data,isinstance=turf_object)

        if serializer_instance.is_valid():

            #cleaned_data = serialized_instance.validated_data

             #Turf.objects.filter(id=pk).update(**cleaned_data)

            serializer_instance.save()

            return Response(serializer_instance.data)
        
        else:

            return Response(serializer_instance.errors)


    def delete(self,request,pk=None):

        qs = Turf.objects.filter(id=pk).delete()

        return Response()
