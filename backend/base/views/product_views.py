from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Club
from base.products import products
from base.serializers  import ClubSerializer

from rest_framework import status


@api_view(['GET'])
def getProducts(request):
    products = Club.objects.all()
    serializer = ClubSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Club.objects.get(_id=pk)
    serializer = ClubSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    product = Club.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        countInStock=0,
        organization='',
        gameCategory='',
        addressLine1='',
        addressLine2='',
        city='chennai',
    )
    serializer = ClubSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Club.objects.get(_id=pk)

    product.name = data['name']
    product.price = data['price']
    product.countInStock = data['countInStock']
    product.description = data['description']

    product.save()

    serializer = ClubSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Club.objects.get(_id=pk)
    product.delete()
    return Response('Product was Deleted')