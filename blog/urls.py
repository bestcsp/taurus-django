from django.urls import path
from .views import (about,
                promotion,
                PostListView,
                #PostDetailView,
                PostCreateView,
                PostUpdateView,
                PostDeleteView,
                UserPostListView,
                comment,
                detail,
                )
urlpatterns = [
    #path('',views.home,name='home'),
    path('about',about,name='about'),
    path('promotion',promotion,name='promotion'),
#viewtype
    path('',PostListView.as_view(),name='home'),
    #path('post/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('<int:pk>/',detail,name='detail'),
    path('post/new/',PostCreateView.as_view(),name='create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='delete'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user'),
    path('comment/',comment,name='comment'),
]