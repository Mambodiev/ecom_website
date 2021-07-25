from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
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
from core.views import (
    change_language,
)


urlpatterns = [
    path('change_language/',change_language,name='change_language'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('', views.home, name='home'),
    path(_('contact/'), views.ContactView.as_view(), name='contact'),
    path(_('about/'), views.AboutView.as_view(), name='about'),
    path(_('privacy_policy/'), views.Privacy_policyView.as_view(), name='privacy_policy'),
    path(_('shipping_returns/'), views.Shipping_returnsView.as_view(), name='shipping_returns'),
    path(_('faq/'), views.FaqView.as_view(), name='faq'),
    path(_('terms_of_use/'), views.Terms_of_useView.as_view(), name='terms_of_use'),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path("cart/", include("cart.urls", namespace='cart')),
    path(settings.ADMIN_URL, admin.site.urls),
    path("staff/", include("staff.urls", namespace="staff")),
    path("users/", include("ecom.users.urls", namespace="users")),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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
