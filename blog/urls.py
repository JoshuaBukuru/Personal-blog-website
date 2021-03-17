from django.urls import path
from .import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView,
	UserPostListView
	)
urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), #uses posts form tmeplate
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), #template with a form
    path('post/new/', PostCreateView.as_view(), name='post-create'),  #uses posts form tmeplate
    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
    
]
