from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GoodViewSet, RegistrationViewSet, LoginViewSet, CategoryViewSet

router = DefaultRouter()
router.register('comment', CommentViewSet, basename='comment')
router.register('good', GoodViewSet, basename='good')
router.register('category', CategoryViewSet)
# router.register('registration', RegistrationViewSet, basename='registration')
# router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('registration/', RegistrationViewSet.as_view(), name='registration'),
    path('login/', LoginViewSet.as_view(), name='login'),
    path('', include(router.urls))
]
