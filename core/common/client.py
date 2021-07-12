from django.urls import reverse


class ApiClient:
    def __init__(self, client):
        self.client = client

    def get_users(self, ):
        endpoint = reverse('user-list')
        return self.client.get(endpoint)

    def force_login(self, user):
        return self.client.force_login(user)
