from rest_framework.test import APIClient
from rest_framework import status
from django.test import TransactionTestCase
from django.urls import reverse


# Models
from authentication.models import User

# Create your tests here.


class MyAPITestCase(TransactionTestCase):
    def SetUp(self):
        self.client = APIClient()

    def test_create_student(self):

        # Make the request to the API
        response = self.client.post(
            reverse('user-create'),
            data={
                "name": "Devien George",
                "email": "devien@gmail.com",
                "password": "1234",
                "user_type": 2
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_teacher(self):
        response = self.client.post(
            reverse('user-create'),
            data={
                "name": "Shehab Mohamed",
                "email": "shehab@gmail.com",
                "password": "1234",
                "user_type": 1
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_admin(self):
        response = self.client.post(
            reverse('user-create'),
            data={
                "name": "Ahmed Mohamed",
                "email": "shehab@gmail.com",
                "password": "1234",
                "user_type": 1
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_user(self):
        response = self.client.get(
            reverse('user-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        response = self.client.get(
            reverse('user-detail', kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        users = User.objects.count()
        print(users)

        response = self.client.delete(
            reverse('user-delete', kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
