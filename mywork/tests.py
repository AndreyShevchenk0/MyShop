from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('mywork.urls')),
    ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        """ Checking the response data """

        # For example, it's easier to inspect response.data
    response = self.client.get('/users/4/')
    self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})

    # Instead of inspecting the result of parsing response.content
    response = self.client.get('/users/4/')
    self.assertEqual(json.loads(response.content), {'id': 4, 'username': 'lauren'})

    # Rendering responses
    view = UserDetail.as_view()
    request = factory.get('/users/4')
    response = view(request, pk='4')
    response.render()  # Cannot access `response.content` without this.
    self.assertEqual(response.content, '{"username": "lauren", "id": 4}')
