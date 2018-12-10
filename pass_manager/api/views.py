from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from .models import PassSite
from .serializer import PassSiteSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
import jwt
from datetime import datetime, timedelta


class UserApiView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class PassSiteApiView(APIView):
    serializer_class = PassSiteSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(PassSite.objects.filter(user__id=request.GET['id']), many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        request.data['account_password'] = make_password(request.data['account_password'])
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
        jwt_payload = str(jwt.encode({'user': request.user.id, 'pass_id': request.data['pass_id'], 'exp': datetime.utcnow()+ timedelta(minutes=5)}, 'secret', algorithm='HS256'))
        jwt_payload = jwt_payload[2:]
        jwt_payload = jwt_payload[:-1]
        encoded = jwt.decode(jwt_payload, 'secret', algorithms=['HS256'])
        return JsonResponse({'token': jwt_payload}, status=status.HTTP_201_CREATED)