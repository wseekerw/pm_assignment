import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.utils.config import ROOT_URL

class ReturnPosts(APIView):
    def get(self, request):
        try:
            response = requests.get(ROOT_URL + '/posts/')
            response.raise_for_status()
            posts = response.json()

            return Response(posts, status=status.HTTP_200_OK)

        except requests.RequestException as error:
            return Response({'error': str(error)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)