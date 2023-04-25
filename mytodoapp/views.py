from rest_framework.views import APIView
from rest_framework.response import Response
from mytodoapp.models import CustomUser, Todo
from mytodoapp.serializers import TodoSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class TodoAV(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            # return Response({'error': "Todo does not exist"}, status=status.HTTP_404_NOT_FOUND)
            raise Http404
        
    
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            todo = Todo.objects.get(id = id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many= True)
        return Response(serializer.data)

    
    
    #forv new todo
    def post (seft, request, format=None):
    
        data = request.data

        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messg": "succrssfully Posted" , "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
    
    
    #for updation of todo
    def put(self, request, pk, format=None):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = TodoSerializer(todo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "updated successfully", "Data":serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    # for partial update
    def patch(self, request, pk, format=None):
        id = pk
        todo = self.get_object(id)
        serializer = TodoSerializer(todo, data=request.data, partial= True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "partial updated successfully", "Data":serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response({"msg": "successfully deleted"},status=status.HTTP_204_NO_CONTENT)
    
        
    