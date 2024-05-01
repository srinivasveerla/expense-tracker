from rest_framework.viewsets import ModelViewSet
from ..models import BalanceSheets
from .serializers import BalanceSheetsSerializer

class BalanceSheetViewSet(ModelViewSet):
    queryset = BalanceSheets.objects.all()
    serializer_class = BalanceSheetsSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        custom_param = self.request.query_params.get('uid')
        if custom_param:
            queryset = queryset.filter(user_id=custom_param)
        return queryset