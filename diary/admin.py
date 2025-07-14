from django.contrib import admin
from .models import Diary # models.pyからDiaryクラスをインポート

admin.site.register(Diary)    # DjangoAdminにDiaryクラスを登録