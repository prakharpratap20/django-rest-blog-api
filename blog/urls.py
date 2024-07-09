from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include("apps.posts.urls.web_urls")),
    path('api/posts/', include("apps.posts.urls.api_urls"))
]
