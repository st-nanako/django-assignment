from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Diary
from django.db.models.functions import ExtractYear
# DBから年の一覧を取得
def get_year_choices():
    years = Diary.objects.annotate(year=ExtractYear('created_at')) \
                         .values_list('year', flat=True) \
                         .distinct() \
                         .order_by('-year')
    return [(str(y), f"{y}年") for y in years if y is not None]


#Diaryモデル用の入力フォーム
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('description','weather','condition','feeling')
        widgets = {
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'feeling': forms.Select(attrs={'class': 'form-control'}),
        }

        
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

        if(condition is None):
            self.add_error('condition', '体調を選択してください。')
        elif(feeling is None):
            self.add_error('feeling', '気分を選択してください。')
            
            
# SearchFormクラスを定義
class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['year'].choices = get_year_choices()
        
    year = forms.ChoiceField(
        label='年',
        required=False,  # 必須でなくする
        widget=forms.Select
    )

    month = forms.ChoiceField(
        label='月', 
        choices = (
            ('', ''),
            ('1', '１月'),
            ('2', '２月'),
            ('3', '３月'),
            ('4', '４月'),
            ('5', '５月'),
            ('6', '６月'),
            ('7', '７月'),
            ('8', '８月'),
            ('9', '９月'),
            ('10', '１０月'),
            ('11', '１１月'),
            ('12', '１２月'),
        ),
        required=False,
        widget=forms.widgets.Select
    )