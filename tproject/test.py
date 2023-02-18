from io import BytesIO
from PIL import Image

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from users.models import User
from images.models import Image as Img


class ImageUploadTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', account_type='basic')
        self.url = reverse('image-list')
        self.client.force_login(self.user)

    def tearDown(self):
        self.client.logout()
        Img.objects.all().delete()
        User.objects.all().delete()

    def test_upload_image(self):
        img = self._create_image()
        response = self._upload_image(img)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Img.objects.count(), 1)
        self.assertEqual(response.data['thumbnail_200'], f'http://testserver{Img.objects.get().thumbnail_200.url}')

    def test_list_images(self):
        img1 = self._create_image()
        img2 = self._create_image()
        self._upload_image(img1)
        self._upload_image(img2)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def _create_image(self):
        image = Image.new('RGB', (100, 100), (255, 0, 0))
        file = BytesIO()
        image.save(file, 'jpeg')
        file.name = 'test.jpg'
        file.seek(0)
        return SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')

    def _upload_image(self, img):
        data = {'image': img}
        return self.client.post(self.url, data, format='multipart')
