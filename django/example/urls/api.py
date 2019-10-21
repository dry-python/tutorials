from django.urls import include, path
from rest_framework import routers
from example.api.sign_up import SignUpModelViewSet

router = routers.SimpleRouter()
router.register('users', SignUpModelViewSet.as_viewset(), basename='users')
urlpatterns = [
    path('', include(router.urls)),
]