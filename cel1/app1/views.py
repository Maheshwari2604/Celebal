# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
# Create your views here.

# from rest_framework.response import Response
# from rest_framework import serializers, views

# class IncredibleInputSerializer(serializers.Serializer):
#     model_input = serializers.CharField()

# class IncredibleView(views.APIView):

#     def get(self, request):
#         # Validate the incoming input (provided through query parameters)
#         serializer = IncredibleInputSerializer(data=request.query_params)
#         serializer.is_valid(raise_exception=True)

#         # Get the model input
#         data = serializer.validated_data
#         model_input = data["model_input"]

#         # Perform the complex calculations
#         complex_result = model_input + "xyz"

#         # Return it in your custom format
#         return Response({
#             "complex_result": complex_result,
#         })



@api_view(["POST"])
def add(requestdata):
    print('you entered')
    try:
        print('entry')
        value =  json.loads(requestdata.body)
        #n = []
        
        print value
        q = str(value)
        print(q)
        # s = value['a']
        # sum(s)
        # print(s)
        #print('dsd')
        #type(s)
        su = str(sum(value))
        print(su)
        # request.a
        # sum = sum(a)
        # print(sum)
        #sum = json.loads('{"A": a}')
        #r = json.dumps(sum)

        # s1=json.loads(a)
        # s2=json.loads(b)
        # sum = s1 + s2
        # sum = json.loads(sum)
        # print(sum)
        #result = str(sum)
        #print(result)
        # su = {
        #     "su": su
        # }
        return Response({
            "sum" : su,
        })
    except:
        return Response(status.HTTP_400_BAD_REQUEST)

# Create your views here.


