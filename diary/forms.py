from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Diary

#Taskモデル用の入力フォーム
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('description','weather','condition','feeling')
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields["description"].widget.attrs = {'placeholder':'詳細'}
        self.fields["weather"].widget.attrs = {'weather':'天気'}
        self.fields["condition"].widget.attrs = {'condition':'体調'}
        self.fields["feeling"].widget.attrs = {'feeling':'気分'}
        
     # 全体にバリデーションを追加する場合はcleanメソッドを作成する
    def clean(self):
        cleaned_data = super().clean() # 全ての入力データを取得
        condition = cleaned_data.get('condition')
        feeling = cleaned_data.get('feeling')

        if(condition <= 0 or condition > 2):
            self.add_error('condition', '体調は0から2の範囲で入力してください。')
        elif(feeling <= 0 or feeling > 2):
            self.add_error('feeling', '気分は0から2の範囲で入力してください。')