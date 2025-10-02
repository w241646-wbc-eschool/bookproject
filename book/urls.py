from django.urls import path #コード追記（4-5）

from . import views #コード追記（4-5）

urlpatterns = [
  path('', views.index_view, name='index'),  #コード追記（5-2）（P.174）
  path('book/', views.LBView.as_view(), name='list-book'), #コード追記（4-5）
  path('book/<int:pk>/detail/', views.DBView.as_view(), name='detail-book'), #コード追記（4-6）
  path('book/create/', views.CBView.as_view(), name='create-book'), #コード追記（4-9）
  path('book/<int:pk>/delete/', views.DelBView.as_view(), name='delete-book'), #コード追記（4-10）（P.159）
  path('book/<int:pk>/update/', views.UBView.as_view(), name='update-book'), #コード追記（4-11）（P.161）
##  path('logout/', views.logout_view, name='logout'), #コード追記（5-5（P.192））
  path('book/<int:book_id>/review/', views.CRView.as_view(), name='review'), #コード追記（5-7（P.214））
]
