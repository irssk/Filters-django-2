from django.urls import path
from . import views

urlpatterns = [
    path('menuitems/', views.MenuItem_view.as_view()),
    path('menuitems/<int:menuitems_id>', views.MenuItem_view.as_view()),
    path('categories/', views.Category_view.as_view()),
    path('categories/<int:categories_id>', views.Category_view.as_view()),
    ]