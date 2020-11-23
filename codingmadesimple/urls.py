from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bold.urls')),
    path('blog/', include('posts.urls')),
    path('store/', include('store.urls')),
    path('<int:id>/', views.detail_view, name="detail"),
    # path('employee/', include('employee_crud.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

