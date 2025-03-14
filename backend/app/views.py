from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializers
from .models import Notes


# Get all Notes
@api_view(['GET'])
def note_list(request):
    note = Notes.objects.all()
    serializer = NoteSerializers(note, many=True)
    return Response(serializer.data)

# Get a single note
@api_view(['GET'])
def note_detail(request, pk):
    try:
        note = Notes.objects.get(id=pk)
    except Notes.DoesNotExist:
        return Response({"error": "note not found"})    
    serializer = NoteSerializers(note, many=False)
    return Response(serializer.data)

# Creaate a new note
@api_view(['POST'])
def note_create(request):
    if request.method =="POST":
        serializer = NoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# complete update a note
@api_view(['PUT'])
def note_complete_update(request, pk):
    if request.method == 'PUT':
        try:
            note = Notes.objects.get(id=pk)    
            serializer = NoteSerializers(instance=note, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})   
        
# partial update a note
@api_view(['PATCH'])
def note_partial_update(request, pk):
    if request.method == 'PATCH':
        try:
            note = Notes.objects.get(id=pk)    
            serializer = NoteSerializers(instance=note, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}) 
        
# delete a note
@api_view(['DELETE'])
def note_delete(request, pk):
    try:
        note = Notes.objects.get(id=pk)
        note.delete()
        return Response({"message": "note deleted successfully"})
    except Exception as e:
        return Response({"error": str(e)}) 
 