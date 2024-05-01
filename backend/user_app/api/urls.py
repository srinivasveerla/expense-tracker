from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

user_router = DefaultRouter()
user_router.register('user',CustomUserViewSet)

# urlpatterns = [
#     path('',CustomUserViewSet.as_view())
# ]