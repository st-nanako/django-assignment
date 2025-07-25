from django.shortcuts import render,redirect
from django.views import View # クラスベースビューを継承するのに必要
from .models import Diary
from .forms import DiaryForm
from django.views import generic    # 汎用ビューのインポート


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

# 詳細
class DetailView(View):
    def get(self,request,pk):
        form = Diary.objects.get(id = pk)
        #テンプレートのレンダリング処理
        return render(request,"diary/detail.html",{'form':form})

detail = DetailView.as_view()

# 追加
class AddView(View):
    def get(self,request):
        #空のフォームを作ってテンプレートに返す
        form = DiaryForm()
        #テンプレートのレンダリング処理
        return render(request,"diary/editAdd.html",{'form' : form})
    
    def post(self,request,*args,**kwargs):
        #登録処理
        #入力データをフォームに渡す
        form = DiaryForm(request.POST)
        #入力データに誤りがないかチェック
        is_valid = form.is_valid()
        
        #データが正常であれば
        if is_valid:
            #モデルに登録
            form.save()
            return redirect('/')
        
        #データが正常じゃない
        return render(request,'diary/editAdd.html',{'form':form})
    
add = AddView.as_view()
