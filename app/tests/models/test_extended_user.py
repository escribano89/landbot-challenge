from django.test import TestCase
from tests.utils import create_and_validate_custom_user
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from landbot.models import ExtendedUser
from unittest import mock


class UserExtendedTest(TestCase):

    def test_given_right_user_when_create_then_returns_right_user(self):
        email = 'test@test.test'
        phone = '+41524204242'
        first_name = 'Javier'
        origin = 'landbot'

        user = create_and_validate_custom_user()

        self.assertEqual(user.phone, phone)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.origin, origin)

    def test_given_wrong_email_when_creating_then_validation_error(self):
        with self.assertRaises(ValidationError):
            create_and_validate_custom_user(email='wrong_email')

    def test_given_wrong_when_creating_then_validation_error(self):
        with self.assertRaises(ValidationError):
            create_and_validate_custom_user(phone='42')

    def test_given_origin_not_provided_when_creating_then_integrity_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_user(origin=None)

    def test_given_email_not_provided_when_creating_then_integrity_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_user(email=None)

    def test_given_phone_not_provided_when_creating_then_integrity_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_user(phone=None)

    def test_given_first_name_not_provided_when_creating_then_integrity_error(self):
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_user(first_name=None)

    def test_given_existing_email_when_creating_then_integrity_error(self):
        create_and_validate_custom_user(email='first@test.test')
        with self.assertRaises(IntegrityError):
            create_and_validate_custom_user(email='first@test.test')
