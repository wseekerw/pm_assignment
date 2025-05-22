import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.utils.handlers_anomalies import (
    filter_shorter_title_posts,
    find_duplicate_titles_by_user,
    find_users_with_similar_titles
    )
from posts.utils.config import ROOT_URL
from posts.utils.fetch_users import fetch_users


class ReturnAnomalies(APIView):
    def get(self, request):
        try:
            response = requests.get(ROOT_URL + '/posts/')
            response.raise_for_status()
            posts = response.json()

            users = fetch_users()

            # Map userId to name
            user_id_to_name = {user['id']: user['name'] for user in users}

            short_titles = filter_shorter_title_posts(posts)
            duplicates = find_duplicate_titles_by_user(posts)
            similar_titles = find_users_with_similar_titles(posts)
            #breakpoint()

            all_anomalies = short_titles + duplicates + similar_titles
            #breakpoint()

            unique_anomalies = []
            seen = set()
            for post in all_anomalies:
                key = (post['userId'], post['id'], post.get('reason'))
                if key not in seen:
                    seen.add(key)
                    unique_anomalies.append(post)

            # usernames
            for post in unique_anomalies:
                 post['username'] = user_id_to_name.get(post['userId'], 'Unknown')

            return Response(unique_anomalies, status=status.HTTP_200_OK)

        except requests.RequestException as error:
            return Response({'error': str(error)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


