from django.views.decorators.http import require_http_methods
from dependencies import Injector, Package, operation
from dependencies.contrib.rest_framework import model_view_set
from example.serializers.category import CategorySerializer
from example.models import Category


implemented = Package("example.implemented")


#TODO: Allow only GET method or create all
@model_view_set
class CategoryListModelViewSet(Injector):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    list = implemented.ListCategories.list