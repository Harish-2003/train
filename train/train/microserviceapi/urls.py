from django.urls import path
from . import views
urlpatterns=[
    #path('hey',views.books)
    path('hey',views.BookList.as_view()),
]