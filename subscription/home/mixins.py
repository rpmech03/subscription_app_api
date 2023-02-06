from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import (Blog)
from rest_framework.decorators import action

class BlogMixin:

    @action(detail=True, methods= ['get'])
    def blog_detail(self, request, pk):
        # print(pk)
        try:
            blog_obj = Blog.objects.get(pk=pk)
            return Response({
                'status' : True,
                'message' : 'blog fetched',
                'data': self.serializer_class(blog_obj).data
            })

        except Exception as e:
               return Response({
                'status' : False,
                'message' : 'invalid uid',
                'data': {}
            })