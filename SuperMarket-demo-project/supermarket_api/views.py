from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Category, SubCategory, Item
from .serializers import CategorySerializer, SubCategorySerializer, ItemSerializer

class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class SubCategoryList(APIView):


    def get(self, request, format=None):
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubCategoryDetail(APIView):


     def get_object(self, pk):
          try:
             return SubCategory.objects.get(pk=pk)
          except SubCategory.DoesNotExist:
             raise Http404

     def get(self, request, pk, format=None):
         subcategory = self.get_object(pk)
         serializer = SubCategorySerializer(subcategory)
         return Response(serializer.data)

class ItemList(APIView):

    def get(self, request, format=None):
        items = Item.objects.all()        
        # for item in items:
        #     print(item.category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):


     def get_object(self, pk):
        try:
           return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
           raise Http404

     def get(self, request, pk, format=None):
         item = self.get_object(pk)
         serializer = ItemSerializer(item)
         return Response(serializer.data)

     def put(self, request, pk, format=None):
         item = self.get_object(pk)
         serializer = ItemSerializer(item, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk, format=None):
         item = self.get_object(pk)
         item.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


