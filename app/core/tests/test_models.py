from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@emailprovider.com'
        password = 'TestPassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the email provider is normalized"""
        email = 'test@EMAILPROVIDER.com'
        user = get_user_model().objects.create_user(
            email, 'testpassword'
        )

        self.assertEqual(user.email, email.lower())
