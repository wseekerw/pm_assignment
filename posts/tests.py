from unittest.mock import patch, Mock
from rest_framework.test import APITestCase
from rest_framework import status

class ReturnPostsViewTest(APITestCase):
    
    @patch('posts.views.posts_view.requests.get')
    def test_return_posts_success_format(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "test title",
                "body": "test body"
            },
            {
                "userId": 2,
                "id": 2,
                "title": "another title",
                "body": "another body"
            }
        ]
        mock_get.return_value = mock_response

        response = self.client.get('/api/posts/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        for post in response.data:
            self.assertIn("userId", post)
            self.assertIn("id", post)
            self.assertIn("title", post)
            self.assertIn("body", post)

class ReturnAnomaliesViewTest(APITestCase):

    @patch('posts.views.anomalies_view.requests.get')
    @patch('posts.views.anomalies_view.fetch_users')
    @patch('posts.utils.handlers_anomalies.filter_shorter_title_posts')
    @patch('posts.utils.handlers_anomalies.find_duplicate_titles_by_user')
    @patch('posts.utils.handlers_anomalies.find_users_with_similar_titles')
    def test_anomalies_format(
        self, mock_similar, mock_duplicates, mock_short, mock_fetch_users, mock_get
    ):
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = [
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "some body"
            }
        ]

        mock_fetch_users.return_value = [{"id": 1, "name": "Leanne Graham"}]
        mock_short.return_value = [
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "some body",
                "reason": "Short title"
            }
        ]
        mock_duplicates.return_value = []
        mock_similar.return_value = []

        response = self.client.get('/api/anomalies/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        for anomaly in response.data:
            self.assertIn("userId", anomaly)
            self.assertIn("id", anomaly)
            self.assertIn("title", anomaly)
            self.assertIn("body", anomaly)
            self.assertIn("reason", anomaly)
            self.assertIn("username", anomaly)            