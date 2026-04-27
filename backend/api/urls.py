from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, SchemeViewSet, BuyerViewSet, LoginView, UserProfileView, LogoutView, RegisterView

router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'schemes', SchemeViewSet)
router.register(r'buyers', BuyerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/me/', UserProfileView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
]
