from .models import UserProfile
from .models import Transaction
from rest_framework  import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'from_user', 'to_user', 'amount']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username', 'email', 'balance']
        

        