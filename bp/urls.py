from django.conf import settings #コード変更（5-8（P.239））
from django.conf.urls.static import static #コード変更（5-8（P.239））
from django.contrib import admin
from django.urls import path, include #コード追記

urlpatterns = [
    path('admin/', admin.site.urls),
##    path('accounts/', include('django.contrib.auth.urls')), #コード追記（5-4（P.185））
    path('accounts/', include('accounts.urls')), #コード変更（5-6（P.199））
    path('', include('book.urls')), #コード追記
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
##urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #コード変更（5-8（P.239））
