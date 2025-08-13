from django.urls import path
from diary import views as diary
from .views import search

urlpatterns = [
    path("", diary.index,name="index"),
    
    path("detail/<int:pk>/", diary.detail,name="detail"), # データ詳細
    path("editAdd/", diary.add,name="add"), # データ登録
    path("editAdd/<int:pk>/",diary.edit,name="edit"), #データ編集
    path('delete/<int:pk>/', diary.delete, name="delete"),  # データ削除ページ 
    path('search/', diary.search, name="search"),  # データ検索ページ 
]