from balancesheet_entry.api.urls import entry_router
from balancesheet.api.urls import balancesheet_router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from user_app.api.urls import user_router


router = DefaultRouter()

# user
router.registry.extend(user_router.registry)

# balancesheets
router.registry.extend(balancesheet_router.registry)

# balancesheet entries
router.registry.extend(entry_router.registry)



urlpatterns = [
    path('',include(router.urls))
]