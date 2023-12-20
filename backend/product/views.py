from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework import generics, mixins, permissions, authentication
from .permissions import IsStaffPermission

# Create your views here.

@api_view(['POST', 'GET'])
def api_view(request):
    # query = Product.objects.all().order_by('?').first()
    data = ProductSerializer(data=request.data)
    if data.is_valid(raise_exception=True):
      data.save()
      return Response(data.data)
    else:
      return Response({'details': 'instance is not valid'})
        
    # if query:  770901965
    #   #  data=model_to_dict(query, fields=['id', 'name', 'price'])
    #   data = ProductSerializer(query).data

class DetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateApiView(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
   permission_classes = [IsStaffPermission]

   def perform_create(self, serializer):
      name= serializer.validated_data.get('name')
      content = serializer.validated_data.get('content') or None
      if content is None:
         content = name
      serializer.save(content=content)
class UpdateApiView(generics.UpdateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer

class DeleteApiView(generics.DestroyAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer

class ProductMixinsView(generics.GenericAPIView, 
         mixins.CreateModelMixin, 
         mixins.DestroyModelMixin, 
         mixins.RetrieveModelMixin,
         mixins.ListModelMixin,
         mixins.UpdateModelMixin
            ):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
   permission_classes = [IsStaffPermission]

   def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)
   
   def get(self, request, *args, **kwargs):
      pk = kwargs.get('pk')
      if pk is not None:
         return self.retrieve(request, *args, **kwargs)
      return self.list(request, *args, **kwargs)
   
   def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

   def patch(self, request, *args, **kwargs):
      return self.partial_update(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)