from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.views.generic import View
from django.shortcuts import render, get_object_or_404 
from rest_framework import status
        
class Student(APIView):        
  def get(request):
      id=request.query.params.get("id")
     

class DetailsAPIView(APIView):
     def get(self, request, id=None):
        if id is not None:
            try:   
                  person = Person.objects.get(pk=id)
                  person_serializer = PersonSerializer(person)
                  hobby = Interest.objects.filter(person_interest=person)
                  hobby_serializer = InterestSerializer(hobby, many=True)
                  s_address = PersonAddress.objects.filter(person_id=person) 
                  s_address_serializer = PersonAddressSerializer(s_address, many=True)

                  data = [{
                      'person': person_serializer.data,
                      'hobbys': hobby_serializer.data,
                      's_address': s_address_serializer.data,
                  }]

                  return render(request, 'home.html', {"persons":data})
            except Person.DoesNotExist:
              # Render the template with a message for invalid ID
              return render(request, 'home.html', {'message': 'Invalid ID '}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = []
            persons = Person.objects.all()
            for person in persons:
              instance_data = {"name":person.name,"age":person.age}
              instance_data["hobbies"] = [interest.title for interest in person.interest.all()]
              instance_data["s_addresses"] = PersonAddressSerializer(person.person_details).data
              data.append(instance_data)


            return render(request, 'base.html', {"persons":data})


class CreatePersonAPIView(APIView):
    def post(self, request):
        person_serializer = PersonSerializer(data=request.data)
        if person_serializer.is_valid():
            person_serializer.save()
            return render(request,'post.html',person_serializer)
            
            