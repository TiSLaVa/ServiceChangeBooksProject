import requests

from rest_framework.response import Response
from rest_framework.views import APIView


class ActivateUser(APIView):
    """Активация пользователя по ссылке на почте."""
    def get(self, request, uid, token):
        payload = {'uid': uid, 'token': token}
        url = "http://localhost:8000/auth/users/activation/"
        result = requests.post(url, data=payload)
        return Response(result.text)
