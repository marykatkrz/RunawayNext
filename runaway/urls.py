from django.urls import path

from . import views

app_name='runaway'

urlpatterns=[
    path('', views.PostListView.as_view(), name="home"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('profiles/post/create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('profiles/<int:pk>/comment/', views.CommentView.as_view(), name='add_comment'),
    path('profiles/<int:pk>/delete', views.CommentDeleteView.as_view(),name='delete_comment'),
    path('profiles/<int:pk>/edit', views.CommentUpdateView.as_view(), name='edit_comment'),
] 