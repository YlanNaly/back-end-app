from django.contrib.staticfiles.views import serve
from django.shortcuts import redirect
from django.urls import re_path, path
from source.views import login_view
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('help/contact/9417940251527349', lambda request: redirect('/')),
    path('login', login_view, name='login'),  # Updated login URL path
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

# Add a URL pattern to serve media files (if needed)
if settings.DEBUG and settings.MEDIA_URL != '/media/':
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
