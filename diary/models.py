from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User # Userモデルをインポート

# Create your models here.

class Diary(models.Model):
    class Meta: # DBに関する設定を指定できる内部クラス（並び順、表示名、テーブル名、制約を指定できる）
        db_table = 'diaries' # 使用するテーブル名を指定（省略すると自動で app_model 名になる）
    
    # verbose_name：人間にとってわかりやすい名前（ラベル）」を指定するためのオプション ※ カラム名は変更されずtitleのまま
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name="作成日",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日",auto_now=True,null=True)
    description = models.TextField(verbose_name="詳細", null=True, blank=True)
    weather = models.CharField(verbose_name="天気", max_length=255)
    condition = models.IntegerField(verbose_name="体調", default=0,validators=[MinValueValidator(0), MaxValueValidator(2)])
    feeling = models.IntegerField(verbose_name="気分", default=0,validators=[MinValueValidator(0), MaxValueValidator(2)])
     
    def __str__(self): # 管理画面でレコード毎に表示する文字列を指定
        return f'{self.created_at}'