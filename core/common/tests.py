from django.test import TestCase

from core.common.asserter import ApiResponseAssertionBuilder
from core.common.client import ApiClient


class GenericTestCase(TestCase):
    assertion_builder_cls = ApiResponseAssertionBuilder

    def setUp(self) -> None:
        self.api_client = ApiClient(self.client)
        super().setUp()

    def assert_that(self, val, description=''):
        return self.assertion_builder_cls(val, description)
