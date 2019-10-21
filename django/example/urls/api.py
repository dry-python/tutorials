from django.urls import include, path
from rest_framework import routers
from example.api.sign_up import SignUpModelViewSet
from example.api.category_list import CategoryListModelViewSet

router = routers.SimpleRouter()
router.register('users', SignUpModelViewSet.as_viewset(), basename='users')
router.register('categories', CategoryListModelViewSet.as_viewset(), basename='categories')
urlpatterns = [
    path('', include(router.urls)),
]