from django.contrib import admin

# Register your models here.

# ↓ 管理画面で「SampleModel」を、認識・表示させるために記述
# from .models import SampleModel #コード追記
# admin.site.register(SampleModel) #コード追記

# ↓ 作成したモデル「Book」を、管理画面に反映させるために記述
from .models import Book, Review #コード追記（5-7（P.224））

admin.site.register(Book) #コード追記
admin.site.register(Review) #コード追記（5-7（P.224））
