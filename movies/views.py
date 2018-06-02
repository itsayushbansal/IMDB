from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .import models as movies_models
from . import permissions as movies_permissions
from .import serializers as movies_serializers
# Create your views here.


class Movie(APIView):
    """

    """
    permission_classes = (movies_permissions.IsAuthenticatedAndAdmin,)

    def get(self,request):
        """

        :param request:
        :return:
        """
        movies = movies_models.Movie.objects.filter(is_deleted=False)
        movie_get_serializer = movies_serializers.MovieSerializer(movies,many=True)
        return Response(data={'data':movie_get_serializer.data},status=status.HTTP_200_OK)

    def post(self,request):
        """

        :param request:
        :return:
        """
        movie_serializer = movies_serializers.MovieSerializer(data=request.data)
        if not movie_serializer.is_valid():
            return Response(data={'error':movie_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        movie_serializer.save()
        return Response(data={'message':'Saved Successfully'},status=status.HTTP_200_OK)

    def put(self,request):
        """

        :param request:
        :return:
        """
        if not (request.data.get('movie_id') and isinstance(request.data['movie_id'],int)):
            return Response(data={'error':'movie_id is a required field/movie_id should be integer'},
                            status=status.HTTP_400_BAD_REQUEST)
        movie_obj = movies_models.Movie.objects.filter(id=request.data['movie_id'],is_deleted=False).first()
        if not movie_obj:
            return Response(data={'error':'Invalid movie_id'},status=status.HTTP_400_BAD_REQUEST)
        movie_edit_serializer = movies_serializers.MovieSerializer(movie_obj,data=request.data,partial=True)
        if not movie_edit_serializer.is_valid():
            return Response(data={'error':movie_edit_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        movie_edit_serializer.save()
        return Response(data={'message':'Changes Saved Successfully'},status=status.HTTP_200_OK)

    def delete(self,request):
        """

        :param request:
        :return:
        """
        if not (request.data.get('movie_id') and isinstance(request.data['movie_id'],int)):
            return Response(data={'error':'movie_id is a required field/movie_id should be integer'},
                            status=status.HTTP_400_BAD_REQUEST)
        movie_obj = movies_models.Movie.objects.filter(id=request.data['movie_id'],is_deleted=False).first()
        if not movie_obj:
            return Response(data={'error':'Invalid movie_id'},status=status.HTTP_400_BAD_REQUEST)
        movie_obj.delete()
        return Response(data={'message':'Deleted Successfully'},status=status.HTTP_200_OK)