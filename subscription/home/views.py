from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import (Blog)
from rest_framework.decorators import action
from . import mixins

class BlogView(viewsets.ModelViewSet, mixins.BlogMixin):
    queryset = Blog.objects.all()
    # serializer_class = BlogSerializer #ab post kruga to error dega cz blog_title n uid send kr rha hu n iske 
                                    # alawa kch or send kruga to error dega islye m blogdetailserializer ka use kruga.
    serializer_class = BlogDetailSerializer
    
    def list(self, request, *args, **kwargs):
        return Response({
            'status' : True,
            'message' : 'blogs fetched',
            'data': {
            'count' :  self.queryset.count(), #by this can access queryset
            # 'blogs' : self.serializer_class(self.queryset, many = True).data #can access serializer_class
            'blogs' : BlogSerializer(self.queryset, many = True).data
            }
        })

    # @action(detail=False, methods= ['get'])
    # def blog_detail(self, request, pk=None):

    #     return Response({
    #         'status' : True,
    #         'message' : 'blogs detail',
    #         'data': {}
    #     })

   
