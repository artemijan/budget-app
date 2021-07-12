from django.test import TestCase

# Create your tests here.
from core.common.tests import GenericTestCase
from core.customer.factory import UserFactory


class UserTestCase(GenericTestCase):
    def test_get_user_is_ok(self):
        # given
        user = UserFactory(is_staff=True)
        self.api_client.force_login(user)
        # when
        response = self.api_client.get_users()
        # then
        self.assert_that(response).is_ok()
        self.assert_that(response).extracting_body('results').is_length(1)
