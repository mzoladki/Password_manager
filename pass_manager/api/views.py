from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from .models import PassSite
from .serializer import PassSiteSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
import jwt
from datetime import datetime, timedelta
import base64


class PassSiteApiView(APIView):
    serializer_class = PassSiteSerializer

    def get(self, request, format=None):
        data = PassSite.objects.filter(user__id=request.GET['id'])
        for d in data:
            d.account_password = str(base64.b64decode(d.account_password))[2:-1]
        serializer = self.serializer_class(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        request.data['account_password'] = str(base64.b64encode(request.data['account_password'].encode()))[2:-1]
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PassSiteDetailApiView(APIView):
    serializer_class = PassSiteSerializer

    def get_object(self, pk, user):
        return get_object_or_404(PassSite, user=user, pk=pk)

    def get(self, request, format=None):
        pass_site = self.get_object(request.data['id'], request.user)
        serializer = self.serializer_class(pass_site)
        return Response(serializer.data)
    
    def put(self, request, format=None):
        pass_site = self.get_object(request.data['id'], request.user)
        request.data['account_password'] = str(base64.b64encode(request.data['account_password'].encode()))[2:-1]
        serializer = self.serializer_class(pass_site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        pass_site = self.get_object(request.GET.get('pk',''), request.user)
        pass_site.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreatePassSiteShareApiView(APIView):

    def post(self, request, format=None):
        print(request.data)
        request.data['exp'] = datetime.utcnow()+ timedelta(minutes=5)
        jwt_payload = str(jwt.encode(request.data, 'secret', algorithm='HS256'))[2:-1]
        print(jwt_payload)
        return JsonResponse({'token': jwt_payload}, status=status.HTTP_201_CREATED)