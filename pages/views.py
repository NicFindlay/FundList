from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()
# class PagesView(LoginRequiredMixin, TemplateView):
class PagesView(TemplateView):
    pass


#  Authentication
pages_authentication_login_view = PagesView.as_view(
    template_name="pages/authentication/auth-login.html"
)
pages_authentication_register_view = PagesView.as_view(
    template_name="pages/authentication/auth-register.html"
)
pages_authentication_recoverpw_view = PagesView.as_view(
    template_name="pages/authentication/auth-recoverpw.html"
)
pages_authentication_lockscreen_view = PagesView.as_view(
    template_name="pages/authentication/auth-lock-screen.html"
)
pages_authentication_logout_view = PagesView.as_view(
    template_name="pages/authentication/auth-logout.html"
)
pages_authentication_confirm_mail_view = PagesView.as_view(
    template_name="pages/authentication/auth-confirm-mail.html"
)
pages_authentication_email_verification_view = PagesView.as_view(
    template_name="pages/authentication/auth-email-verification.html"
)
pages_authentication_two_step_verification_view = PagesView.as_view(
    template_name="pages/authentication/auth-two-step-verification.html"
)
#  Pages
pages_starter_page_view = PagesView.as_view(template_name="pages/pages-starter.html")
pages_maintenance_view = PagesView.as_view(template_name="pages/pages-maintenance.html")
pages_comingsoon_view = PagesView.as_view(template_name="pages/pages-comingsoon.html")
pages_timeline_view = PagesView.as_view(template_name="pages/pages-timeline.html")
pages_faqs_view = PagesView.as_view(template_name="pages/pages-faqs.html")
pages_pricing_view = PagesView.as_view(template_name="pages/pages-pricing.html")
pages_error_404_view = PagesView.as_view(template_name="pages/pages-404.html")
pages_error_500_view = PagesView.as_view(template_name="pages/pages-500.html")


# Horizontal
pages_horizontal_layout_view = PagesView.as_view(
    template_name="pages/horizontal/layouts-horizontal.html"
)
