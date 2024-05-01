from rest_framework.serializers import ModelSerializer
from ..models import BalanceSheets

class BalanceSheetsSerializer(ModelSerializer):
    class Meta:
        model = BalanceSheets
        fields = ('id','user_id','title')