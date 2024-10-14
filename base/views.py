from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import advocate_serializer
from django.db.models import Q


# Create your views here.
@api_view(["GET","POST","PUT"])
def enpoint(request):
    data=["/avocates","avovates/:username"]

    return Response(data)

@api_view(["GET","POST"])
def list_avocates(request):
    #handel Get Request
    if request.method=='GET':
        query=request.GET.get('query')
        if query ==None:
            query =''
        advocates=Advocate.objects.filter( Q(username__icontains=query)| Q(bio__icontains=query))
        serializer=advocate_serializer(advocates,many=True)
        return Response(serializer.data)

    if request.method=="POST":

        advocate= Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )

        serializer=advocate_serializer(advocate,many=False)

        return Response(serializer.data)





@api_view(["GET","PUT","DELETE"])
def avocate_details(request,pk):


    advocate=Advocate.objects.get(id=pk)

    #Handel Get
    if request.method=="GET":

        serializer=advocate_serializer(advocate,many=False)

        return Response(serializer.data)
    
    if request.method=="PUT":

        advocate.username=request.data["username"]
        advocate.bio=request.data["bio"]
        advocate.save()


        serializer=advocate_serializer(advocate,many=False)
        return Response(serializer.data)

    if request.method=="DELETE":

        advocate.delete()
        return Response('user was deleted')



