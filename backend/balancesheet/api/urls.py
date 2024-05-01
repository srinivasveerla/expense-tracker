from rest_framework.routers import DefaultRouter
from .views import BalanceSheetViewSet

balancesheet_router = DefaultRouter()
balancesheet_router.register('balancesheet',BalanceSheetViewSet)