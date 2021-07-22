from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from core import views
from django.utils.translation import gettext_lazy as _



urlpatterns = [
    path('', views.HomeViews.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path("cart/", include("cart.urls", namespace='cart')),
    path(settings.ADMIN_URL, admin.site.urls),
    path("staff/", include("staff.urls", namespace="staff")),
    path("users/", include("ecom.users.urls", namespace="users")),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    path("api/", include("config.api_router")),
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
