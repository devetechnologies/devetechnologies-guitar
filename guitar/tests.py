from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Guitar
# Create your tests here.

class GuitarViewSetTest(APITestCase):
    def  setUp(self):
      """
      Create test data for the tests.
      """

      self.guitar_1 = Guitar.objects.create(
         brand="Fender",
         model="Stratocaster",
         price=1500.00,
         description= "A clasic electric guitar."
      )


      self.guitar_2 = Guitar.objects.create(
         brand="Gibson",
         model="Les Paul",
         price=3500.00,
         description= "A legendary guitar."
      )

      self.valid_payload={
         "brand": "Ibanez",
            "model": "RG Series",
            "price": 1200.00,
            "description": "A modern electric guitar for shredders."
      }

      self.invalid_payload = {
            "brand": "",
            "model": "",
            "price": -1200.00,
            "description": ""
        }

    def test_get_guitars(self):
        """
        Test retrieving the list of guitars.
        """
        url = reverse('guitar-list')  # Automatically resolves the URL for the viewset.
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    ''' def test_get_single_guitar(self):
        """
        Test retrieving a single guitar.
        """
        url = reverse('guitar-detail', kwargs={'pk': self.guitar_1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], self.guitar_1.brand)

    def test_create_guitar_valid(self):
        """
        Test creating a new guitar with valid data.
        """
        url = reverse('guitar-list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Guitar.objects.count(), 3)
        self.assertEqual(Guitar.objects.last().brand, self.valid_payload['brand'])

    def test_create_guitar_invalid(self):
        """
        Test creating a new guitar with invalid data.
        """
        url = reverse('guitar-list')
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_guitar(self):
        """
        Test updating an existing guitar.
        """
        url = reverse('guitar-detail', kwargs={'pk': self.guitar_1.pk})
        new_data = {
            "brand": "Fender",
            "model": "Telecaster",
            "price": 1400.00,
            "description": "Updated description."
        }
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.guitar_1.refresh_from_db()
        self.assertEqual(self.guitar_1.model, "Telecaster")

    def test_delete_guitar(self):
        """
        Test deleting a guitar.
        """
        url = reverse('guitar-detail', kwargs={'pk': self.guitar_1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Guitar.objects.count(), 1)'''