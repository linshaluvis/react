from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import restapi,CustomUser
from .serializers import restserializer,userserializer,loginserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from rest_framework import permissions
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data(request):
    user = restapi.objects.all()
    u = restserializer(user,many=True)
    return Response(u.data)
    


# Create your views here.

class userview(APIView):
    permission_classes =[AllowAny]
    def get(self,request):
        user = restapi.objects.all()
        u = restserializer(user,many=True)
        return Response(u.data)
    def post(self,request):
        serialiser = restserializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        else:
            return Response(serialiser.errors)
        
    def delete(self,request,id):
        if id:
            user = restapi.objects.get(id=id)
            user.delete()
            return JsonResponse({"data":"data deleted"})
        else:
            return JsonResponse({"error":"no such data"})
        
    def put(self,request,id):
        if id :
            user = restapi.objects.get(id=id)
            serialiser = restserializer(data=request.data)
            if serialiser.is_valid():
                user.name = request.data.get('name')
                user.age = request.data.get('age')
                user.course = request.data.get('course')
                user.save()
                return Response(serialiser.data)
            else:
                return Response(serialiser.errors)






@api_view(['GET'])
def home(request):
    user = restapi.objects.all()
    serialiser = restserializer(user,many=True)
    #arr = []
    #for i in user:
    #    username = [{'name':i.name}]
    #    arr.append(username)
    return Response(serialiser.data)
@api_view(['POST'])
def post_data(request):
    serialiser = restserializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['DELETE'])
def delete_data(request):
    id = request.GET.get('id')
    if id:
        user = restapi.objects.get(id=1)
        user.delete()
        return JsonResponse({"data":'data deleted'})
    else:
        return JsonResponse({"error":'give id as param'})
    

@api_view(['POST'])
def register(request):
    serialiser = userserializer(data=request.data)
    if serialiser.is_valid():
            user = CustomUser.objects.create_user(username = request.data.get('username'),password = request.data.get('password'))
            token = Token.objects.create(user=user)
            print(token)
            return Response(serialiser.data)
    else:
            return Response(serialiser.errors)
@api_view(['POST'])
def loginview(request):
    serialiser = loginserializer(data=request.data)
    if serialiser.is_valid():
        
            user = authenticate(username = request.data.get('username'),password = request.data.get('password'))
            print(user)
            if user:
                token = Token.objects.get(user=user)
                return JsonResponse({'token':token.key})
            else:
                return Response(serialiser.errors)




