from django.shortcuts import render
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.reverse import reverse_lazy
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse, StreamingHttpResponse, Http404, FileResponse
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from django.views.generic.edit import CreateView, FormView, UpdateView, FormMixin
from django.views.generic import View, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, render_to_response

from ws.models import Profile
from ws.serializers import ProfileSerializer

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

# Create your views here.
class MultiFileUploadView(APIView):
    """docstring for MultiFileUploadView"""
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    permission_classes = (
        permissions.AllowAny,
    )
    throttle_classes = (
        BurstRateThrottle,
    )
    model = Profile

    def put(self, request, *args, **kwargs):
        file_list = request.FILES.getlist('attach_files')
        if not file_list:
            return Response(
                {"non_field_errors": ["Files are required."]},
                status=status.HTTP_400_BAD_REQUEST
            )
        attach_file = None 
        for _file_ in file_list:
            try:
                attach_file = Profile(
                    file_name=_file_.name[0:100],
                    attach_file=_file_
                )
                attach_file.save()
            except Exception as e:
            	print(e)
                return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ProfileSerializer(attach_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        file_list = request.FILES.getlist('attach_files')
        if not file_list:
            return Response(
                {"non_field_errors": ["Files are required."]},
                status=status.HTTP_400_BAD_REQUEST
            )
        attach_file = None 
        for _file_ in file_list:
            try:
                attach_file = Profile(
                    file_name=_file_.name[0:100],
                    attach_file=_file_
                )
                attach_file.save()
            except Exception as e:
            	print(e)
                return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ProfileSerializer(attach_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PortadaPreviewView(View):
	model = Profile

	def get_object(self):
		id = self.kwargs['id']
		if not self.model.objects.filter(id=id).exists():
			raise Http404
		portada = self.model.objects.get(id=id)
		return portada

	def get(self, request, *args, **kwargs):
		portada = self.get_object()
		image = portada.attach_file.read()
		return HttpResponse(image, content_type="image/jpeg")


