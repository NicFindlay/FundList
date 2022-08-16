"""dason URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from funds import views as fund_views
from fundlist import views as fundlist_views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", fund_views.get_funds),
    path("fund/<str:fund>/", fund_views.get_single_fund, name="fund"),
    path("admin/", admin.site.urls),
    path("apex/", fundlist_views.get_apex),
    # # Dashboard
    path("", fundlist_views.DashboardView.as_view(), name="dashboard"),
    path("settings", fundlist_views.Settings.as_view(), name="settings"),
    # # Custum change password done page redirect
    path(
        "account/password/change/",
        login_required(fundlist_views.MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    # # Custum set password done page redirect
    path(
        "account/password/set/",
        login_required(fundlist_views.MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    # # Pages
    path("pages/", include("pages.urls")),
    # # Include the allauth and 2FA urls from their respective packages.
    path("/", include("allauth_2fa.urls")),
    path("account/", include("allauth.urls")),
    path("run_extraction/", fundlist_views.run_extraction, name="run_extraction"),
    path(
        "calculate_returns/", fundlist_views.calculate_returns, name="calculate_returns"
    ),
]
