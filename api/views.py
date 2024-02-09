from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import authentication,permissions
from api.serializers import UserSerializer,ProductSerializer,BasketItemSerializer,BasketSerializer
from rest_framework.decorators import action
from api.models import Product,BasketItem


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class ProductView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError('permission denied')
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError('permission denied')
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError('permission denied')


    #url:http://127.0.0.1:8000/api/products/{id}/add_to_basket/
    #method:post
    #data:{qty}

    @action(methods=['post'],detail=True)
    def add_to_basket(self, request,*args, **kwargs):
        id=kwargs.get('pk')
        product_obj=Product.objects.get(id=id)
        basket_obj=request.user.cart
        serializer=BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product_obj,basket=basket_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class BasketView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    #url:http://127.0.0.1:8000/api/baskets/
    #method:get
    def list(self, request,*args,**kwargs):
        qs=request.user.cart
        serializer=BasketSerializer(qs,many=False)
        return Response(data=serializer.data)


class BasketItemView(viewsets.ModelViewSet):
    serializer_class=BasketItemSerializer
    queryset=BasketItem.objects.all()

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError('permission denied')

