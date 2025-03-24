from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Promotion, Category, Product
from .serializers import PromotionSerializer, CategorySerializer, ProductSerializer


class PromotionView(ListAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SearchView(APIView):
    def get(self, request):
        q = request.query_params.get('q')
        queryset = Product.objects.filter(name__icontains=q)
        serializer = ProductSerializer(queryset, many=True)
        return Response(data=serializer.data, status=200)
