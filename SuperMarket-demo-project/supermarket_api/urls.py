from django.urls import path
from .views import CategoryList,CategoryDetail,SubCategoryList, SubCategoryDetail,ItemList,ItemDetail

urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='singlecategory'),

    path('subcategories', SubCategoryList.as_view(), name='subcategories'),
    path('subcategories/<int:pk>/', SubCategoryDetail.as_view(), name='singlesubcategory'),

    path('items', ItemList.as_view(), name='items'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='singleitem'),

]
