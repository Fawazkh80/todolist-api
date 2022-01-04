from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def TaskIndex(request):
    allTask = models.Task.objects.all()
    serializer = serializers.TaskSerializer(allTask, many = True )
    return Response({
        'data': serializer.data
    })

@api_view(['POST'])
def CreateTask(request):
    serializer = serializers.TaskSerializer(data={
    'title' : request.data["title"],
    'desc'  : request.data["desc"],
    'box'   : request.data["box"]})

    if serializer.is_valid():
        serializer.save()

    return Response({
        'data': serializer.data
    })

@api_view(['PUT'])
def UpdateTask(request,id):
    oneTask = models.Task.objects.get(id= id) 
    serializer = serializers.TaskSerializer(instance = oneTask,data={
'title' : request.data["title"],
'desc'  : request.data["desc"],
'box'   : request.data["box"]})

    if serializer.is_valid():
        serializer.save()
    return Response({
        'data': serializer.data
    })

@api_view(['DELETE'])
def DeleteTask(request, id):
    oneTask = models.Task.objects.get(id=id)
    oneTask.delete() 
    return Response(True)

@api_view(['POST'])
def CreateBox(request):
    name = request.data["name"]

    serializer = serializers.BoxSerializer(data={
    'name' : name
    })
    

    if serializer.is_valid():
        try:
            oneBox = models.Box.objects.get(name=name)
            print("Already Exist")
        except models.Box.DoesNotExist:
            serializer.save()
            print("Created New")
    

    return Response({
        'data': serializer.data
    })



