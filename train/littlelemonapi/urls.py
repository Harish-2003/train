from django.urls import path
from . import views
urlpatterns=[
    #path('hey',views.books)
    path('menuitem',views.MenuItemsview.as_view()),
]