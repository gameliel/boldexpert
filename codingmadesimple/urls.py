from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from portfolio import views
# from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bold.urls')),
    path('blog/', include('posts.urls')),
    path('<int:id>/', views.detail, name="detailed"),
    path('store/', include('store.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('paystack/', include(('paystack.urls', 'paystack'), namespace='paystack'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


