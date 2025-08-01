from django.shortcuts import render,redirect
from django.views import View # クラスベースビューを継承するのに必要
from .models import Diary
from .forms import DiaryForm,SearchForm
from django.views import generic    # 汎用ビューのインポート
from django.contrib.auth.mixins import LoginRequiredMixin   # LoginRequiredMixinをインポート


# Create your views here.

class IndexView(LoginRequiredMixin,View):
    def get(self, request): # GETリクエストが送信された時に呼び出される
        # diaryリストを取得
        diary_list = Diary.objects.filter(author=self.request.user).order_by('created_at')
        form = SearchForm(request.GET or None)
        context = {"diary_list":diary_list,"form":form}

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
class AddView(LoginRequiredMixin,View):
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

# 編集
class EditView(LoginRequiredMixin,View):
    def get(self,request,pk):
        diary = Diary.objects.get(id = pk)
        diaryform = DiaryForm(instance = diary)
        #テンプレートのレンダリング処理
        return render(request,"diary/editAdd.html",{'form' : diaryform,'diary':diary})
    
    def post(self,request,pk,*args,**kwargs):
        #編集処理
        data = Diary.objects.get(id=pk)
        diaryform = DiaryForm(request.POST, instance = data)
        is_valid = diaryform.is_valid()
        
        #データが正常であれば
        if is_valid:
            #モデルに登録
            diaryform.save()
            return redirect('/')
        
        #データが正常じゃない
        return render(request,'diary/editAdd.html',{'form':diaryform})
    
edit = EditView.as_view()

# 削除
class DeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        form = Diary.objects.get(id = pk)
        #テンプレートのレンダリング処理
        return render(request,"diary/delete.html",{'form':form})
    
    def post(self,request,pk,*args,**kwargs):
        #削除処理
        Diary.objects.filter(id=pk).delete()
        return redirect('/')
        
    
delete = DeleteView.as_view()

# 検索

def search(request):
    form = SearchForm(request.GET or None)
    diaries = Diary.objects.all()

    if form.is_valid():
        year = form.cleaned_data.get('year')
        month = form.cleaned_data.get('month')

        if year:
            diaries = diaries.filter(created_at__year=int(year))
        if month:
            diaries = diaries.filter(created_at__month=int(month))

    return render(request, 'diary/results.html', {'form': form, 'diaries': diaries})