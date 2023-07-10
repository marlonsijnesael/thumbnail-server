from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import TextureImage, Project, Recognizer
from .serializers import TextureSerializer, ProjectSerializer, RecognizerSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser


"""
    Views and helper functions to create projects, textures, and thumbnails
"""


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the editor index.")


# Helper function to append required headers to a response
def append_standard_headers(response):
    response['Vary'] = 'X-Requested-With'
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


class RecognitionViewSet(viewsets.ModelViewSet):
    queryset = Recognizer.objects.all()
    serializer_class = RecognizerSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        response = JsonResponse({'succes!': 'succes'}, status=status.HTTP_201_CREATED, safe=False)
        response = append_standard_headers(response)

        return response

    @method_decorator(csrf_exempt)
    def list(self, request, *args, **kwargs):
        serializer = TextureSerializer(Recognizer.objects.all(), many=True)
        response = JsonResponse(serializer.data, safe=False)
        response = append_standard_headers(response)

        return response


class TextureViewSet(viewsets.ModelViewSet):
    queryset = TextureImage.objects.all()
    serializer_class = TextureSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_extra_actions(self):
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = JsonResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers, safe=False)
        response = append_standard_headers(response)

        return response

    @method_decorator(csrf_exempt)
    def perform_create(self, serializer):
        serializer.save()

    @method_decorator(csrf_exempt)
    def list(self, request, *args, **kwargs):
        queryset = TextureImage.objects.all()
        serializer = TextureSerializer(queryset, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response = append_standard_headers(response)

        return response


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_extra_actions(self):
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = JsonResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers, safe=False)
        response = append_standard_headers(response)

        return response

    @method_decorator(csrf_exempt)
    def perform_create(self, serializer):
        serializer.save()

    @method_decorator(csrf_exempt)
    def list(self, request, *args, **kwargs):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response = append_standard_headers(response)

        return response
