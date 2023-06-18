from .models import UserProfile
from .models import Transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserProfileSerializer
from .serializers import TransactionSerializer



@api_view(['GET', 'POST', 'DELETE'])
def Profile(request): 
    
    if request.method == 'GET':
        Users  = UserProfile.objects.all()
        serializer = UserProfileSerializer(Users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status =  status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Users = UserProfile.objects.all()
        Users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])    
def ProfileInd(request, pk, format=None):
    
    try:
        user = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'POST'])
def Transactionss(request):
    
    if request.method  == 'GET':
        Transactions = Transaction.objects.all()
        serializer = TransactionSerializer(Transactions, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            user1 = serializer.validated_data['from_user']
            user2 = serializer.validated_data['to_user']
            try:
                user1 = UserProfile.objects.get(username=user1.username)
                user2 = UserProfile.objects.get(username=user2.username)
            except UserProfile.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            if user1.balance >= serializer.validated_data['amount']:
                user1.balance -= serializer.validated_data['amount']
                user2.balance += serializer.validated_data['amount']
                user1.save()
                user2.save()
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def TransactionssInd(request, pk):
    
    if request.method == 'GET':
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)