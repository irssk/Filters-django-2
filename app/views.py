from rest_framework.response import Response
from rest_framework import status, request, generics

from .models import MenuItem, Category
from rest_framework.views import APIView
from .serializers import SerializedMenuItem, SerializedCategory

class MenuItem_view(generics.ListAPIView):
    serializer_class = SerializedMenuItem

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset



class Category_view(APIView):

    def get(self, req):
        categories = Category.objects.all()
        serialized_categories = SerializedCategory(categories, many=True)
        data = serialized_categories.data
        return Response(data, status=status.HTTP_200_OK)

