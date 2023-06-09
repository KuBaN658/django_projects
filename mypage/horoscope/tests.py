from django.test import TestCase
from .views import zodiac_dict


class TestHoroscope(TestCase):
    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_sign(self):
        for sign in zodiac_dict.items():
            response = self.client.get(f'/horoscope/{sign[0]}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(f'{sign[1][0]}',
                          response.content.decode())

    def test_sign_number_redirect(self):
        for i, sign in enumerate(zodiac_dict):
            response = self.client.get(f'/horoscope/{i + 1}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{sign}')
