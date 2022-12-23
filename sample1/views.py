# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from django.conf import settings
# import logging
# logger = logging.getLogger(__name__)
#
#
# class StatusView(APIView):
#
#     def get(self, request):
#
#         return {"message": "success"}
from django.http import HttpResponse
import time


async def sample(requests):
    time.sleep(3)
    return HttpResponse("welcome")