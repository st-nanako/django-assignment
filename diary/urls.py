from django.urls import path
from diary import views as mytodo

urlpatterns = [
    path("", mytodo.index,name="index"),
    path("editAdd/", mytodo.add,name="add"), # データ登録
    #path("edit/<int:pk>/",mytodo.edit,name="edit"), #データ編集
    #path('delete/<int:pk>/', mytodo.delete, name="delete"),  # データ削除ページ 
]