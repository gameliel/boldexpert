from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bold.urls')),
    path('blog/', include('posts.urls')),
    path('<int:id>/', views.detail, name="detailed"),
    path('store/', include('store.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


