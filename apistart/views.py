from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Basket, Pantry
from .serializers import PantrySerializer
from .serializers import BasketSerializer

@api_view(['POST'])
def create_pantry(request, basket_id):
    try:
        basket = Basket.objects.get(pk=basket_id)
    except Basket.DoesNotExist:
        return Response({'message': 'Basket not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = PantrySerializer(data=request.data)
        if serializer.is_valid():
            pantry_data = serializer.validated_data
            pantry_data['basket'] = basket
            pantry = Pantry.objects.create(**pantry_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_key_value_store(request, pantry_id):
    try:
        pantry = Pantry.objects.get(pk=pantry_id)
    except Pantry.DoesNotExist:
        return Response({'message': 'Pantry not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        data = request.data
        pantry.key_value_store.update(data)
        pantry.save()
        return Response({'message': 'Key-value pairs added successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_basket_key_value(request, pantry_id, basket_key):
    try:
        pantry = Pantry.objects.get(pk=pantry_id)
    except Pantry.DoesNotExist:
        return Response({'message': 'Pantry not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the specified basket key exists in the pantry's key-value store
    if basket_key in pantry.key_value_store:
        value = pantry.key_value_store[basket_key]
        return Response({'basket_key': basket_key, 'value': value}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Basket key not found in the pantry'}, status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def list_baskets_by_pantry(request, pantry_id):
    try:
        pantry = Pantry.objects.get(pk=pantry_id)
    except Pantry.DoesNotExist:
        return Response({'message': 'Pantry not found'}, status=status.HTTP_404_NOT_FOUND)

    basket_name = request.query_params.get('name', None)
    if basket_name:
        baskets = pantry.baskets.filter(name__icontains=basket_name)
    else:
        baskets = pantry.baskets.all()

    serializer = BasketSerializer(baskets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_basket_key_value(request, pantry_id, basket_key):
    try:
        pantry = Pantry.objects.get(pk=pantry_id)
    except Pantry.DoesNotExist:
        return Response({'message': 'Pantry not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the specified basket key exists in the pantry's key-value store
    if basket_key in pantry.key_value_store:
        new_value = request.data.get('new_value', None)

        if new_value is not None:
            pantry.key_value_store[basket_key] = new_value
            pantry.save()

            return Response({'message': 'Value updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'New value is required'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Basket key not found in the pantry'}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
    
    
@api_view(['DELETE'])
def delete_basket(request, pantry_id, basket_key):
    try:
        pantry = Pantry.objects.get(pk=pantry_id)
    except Pantry.DoesNotExist:
        return Response({'message': 'Pantry not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        basket = pantry.baskets.get(name=basket_key)
    except Basket.DoesNotExist:
        return Response({'message': 'Basket not found in the pantry'}, status=status.HTTP_404_NOT_FOUND)

    basket.delete()
    return Response({'message': 'Basket deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
