from django.db import connection
from django.db.utils import OperationalError
from django.test import TestCase
from django.urls import reverse


class QueryTimeoutWrapper:
    def __call__(self, execute, *args, **kwargs):
        raise OperationalError("Connection timed out")


class HealthyTestCase(TestCase):
    def test_with_working_db_connection(self) -> None:
        response = self.client.get(reverse("healthcheck:healthy"))
        self.assertEqual(response.status_code, 200)

    def test_with_broken_db_connection(self) -> None:
        with connection.execute_wrapper(QueryTimeoutWrapper()):
            response = self.client.get(reverse("healthcheck:healthy"))
            self.assertEqual(response.status_code, 500)
