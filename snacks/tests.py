from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='aseel',
             email='aseel_fawwaz@yahoo.com',
              password='123456'
        )

        self.snack = Snack.objects.create(
            title='Tender',
            purchaser=self.user,
             description='4 Pcs',
        )
    

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'Tender')

    def test_Snack_content(self):
        self.assertEqual(f'{self.snack.title}', 'Tender')
        self.assertEqual(str(self.snack.purchaser), 'aseel')
        self.assertEqual(f'{self.snack.description}', '4 Pcs')
        

    def test_Snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tender')
        self.assertTemplateUsed(response, 'snack_list.html')
    

    def test_Snack_create_view(self):
        response = self.client.post(
            reverse('snack_create'),
            {
                'title': 'Fries',
                'description': 'L',
                'purchaser': self.user.pk,
            }, follow=True
        )

        self.assertRedirects(response, reverse('snack_detail', args='2'))
        self.assertContains(response, 'title')


    def test_Snack_detail_view(self):
        response = self.client.get(reverse('snack_detail', args='1'))
        no_response = self.client.get('/800/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'snack_detail.html')

    

    def test_Snack_update_view_redirect(self):
        response = self.client.post(
            reverse('snack_update', args='1'),
            {'title': 'Potato Fries', 'description': 'XL', 'purchaser': self.user.pk}
        )

        self.assertRedirects(response, reverse('snack_detail', args='1'))

    def test_Snack_delete_view(self):
        response = self.client.get(reverse('snack_delete', args='1'))
        self.assertEqual(response.status_code, 200)