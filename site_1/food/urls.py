from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.indexclassview.as_view(), name = "item"),
    path('<int:pk>/',views.detailclassview.as_view(), name = "detail"),
    path('index/', views.index, name = "food"),
    # add items
    path('add/', views.create_itemclassview.as_view(), name='create_item'),
    #edit items
    path('update/<int:id>', views.update_item, name='update_items'),
    #delete items
    path('delete/<int:id>', views.delete_item, name = "delete_item"),
    
]
