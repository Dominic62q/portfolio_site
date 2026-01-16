# MyPortfolio/urls.py (Main Project URLs)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import both frontend views
from portfolio.views import index, projects_page

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # API endpoints (Prefixed with /api/)
    path("api/", include("portfolio.urls")),

    # Frontend Pages
    path("", index, name="index"),
    path("works/", projects_page, name="projects"), # Added this
]

# Serve media files in both development and production
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT if settings.STATIC_ROOT else None)