from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from posts.utils.config import ROOT_URL
from posts.utils.handlers_summary import generate_summary
from posts.utils.fetch_users import fetch_users


class ReturnSummary(APIView):
    def get(self, request):
        try:
            posts_response = requests.get(ROOT_URL + '/posts/')
            posts_response.raise_for_status()
            posts = posts_response.json()

            users = fetch_users()

            summary = generate_summary(posts, users)
            return Response(summary, status=status.HTTP_200_OK)

        except requests.RequestException as error:
            return Response({'error': str(error)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)