from django.test import TestCase

# Create your tests here.

# tasks/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        response = self.client.post(reverse("task-list"), {"title": "Test Task"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

