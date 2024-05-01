from .views import EntryViewSet
from rest_framework.routers import DefaultRouter

entry_router = DefaultRouter()
entry_router.register('entry',EntryViewSet)
