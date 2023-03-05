from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import Item
from .serializers import ItemSerializer
# Create your views here.


# @csrf_exempt
@api_view(["GET", "POST"])
def items(request: HttpRequest):
    '''
    HTTP 谓词都位于一个方法中, 需要手动判断
    '''
    if request.method == "GET":
        # person = {
        #     "name": "Timothy",
        #     "age": 23,
        # }
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

        return Response({
            "data": serializer.data
        })

    if request.method == "POST":
        print(request.data)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"data": serializer.data},
                status=status.HTTP_201_CREATED)

        return Response(
            data={"message": "Invalid data"},
            status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def item(request: HttpRequest, pk, format=None):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(
            data={"error": "Item does not exist"},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ItemSerializer(item, many=False)
        return Response({
            "data": serializer.data
        })

    if request.method == "PUT":
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data
            })

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        item.delete()
        return Response({
            "message": "Item deleted"
        })


class ItemsView(APIView):
    '''
    APIView

    需要自定义序列化器
    '''

    def get(self, request, pk, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

        return Response({
            "data": serializer.data
        })

    def post(self, request, pk, format=None):
        pass


class ItemsViewMix(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    '''
    mixins, generics

    需要自定义序列化器
    '''

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        data = response.data
        response.data = {"data": data}
        response.status_code = status.HTTP_200_OK
        return response

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return response


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
