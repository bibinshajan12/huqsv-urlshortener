from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('run-tests/', views.run_tests, name='run_tests'),
    path('<str:short_url>/', views.redirect_to_original, name='redirect'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs
    path('saved-urls/', views.view_saved_urls, name='view_saved_urls'),
    path('docs/', views.documentation, name='documentation'),  # Add this line
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static('/docs/', document_root='docs/build/')