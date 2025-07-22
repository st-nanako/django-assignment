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