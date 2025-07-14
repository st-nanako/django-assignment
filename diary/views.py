from django.shortcuts import render
from django.views import View # クラスベースビューを継承するのに必要

# Create your views here.

class IndexView(View):
    def get(self, request): # GETリクエストが送信された時に呼び出される
        # todoリストを取得

        # テンプレートをレンダリング
        return render(request, "diary/index.html")


# ビュークラスをインスタンス化
index = IndexView.as_view()
