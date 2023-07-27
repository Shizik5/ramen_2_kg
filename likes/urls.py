from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="ramen__kg",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('account/', include('account.urls')),
    path('todo_app/', include('todo_app.urls')),
    path('category/', include('category.urls')),
    path('post/', include('post.urls')),
    path('like/', include('like.urls')),
    path('comment/', include('comment.urls')),
    path('recomends/', RecomendView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)