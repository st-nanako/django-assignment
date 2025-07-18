from django.shortcuts import render
from django.views import View # クラスベースビューを継承するのに必要
from .models import Diary

# Create your views here.

class IndexView(View):
    def get(self, request): # GETリクエストが送信された時に呼び出される
        # diaryリストを取得
        diary_list = Diary.objects.order_by('created_at')
        context = {"diary_list":diary_list}

        # テンプレートをレンダリング
        return render(request, "diary/index.html",context)


# ビュークラスをインスタンス化
index = IndexView.as_view()
