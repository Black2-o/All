from django.urls import path
from . import views

urlpatterns=[
    path('', views.homePage, name='home'),
    path('class/', views.classPage, name='class'),
    path('books/<int:pk>/', views.booksPage, name='books'),
    path('chapter/<int:pk>/<int:bpk>', views.chapterPage, name='chapters'),
    path('video-class/<int:cpk>/<int:bpk>/<int:chpk>', views.singleClassPage, name='singleclass'),
    path('video-class/<str:url>', views.singleClassPage, name='singleclass'),

    path('chat/', views.chatPage, name='chat'),

    path('read-books/', views.booksPage, name='readbooks'),


    path('hello/', views.helloworld, name='hello'),
]