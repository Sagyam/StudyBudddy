from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def get_routes(request):
    """
    Returns a list of all the routes in the system.
    """
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/room/:id',

    ]
    return Response(routes)


@api_view(['GET'])
def get_rooms(request):
    """
    Returns a list of all the rooms in the system.
    """
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_room(request, pk):
    """
    Returns details about a room whose id is given.
    """
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
