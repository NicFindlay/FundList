from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView


# Create your views here.
# class AppsView(LoginRequiredMixin, TemplateView):
class AppsView(TemplateView):
    pass


# Ecommerce
apps_ecommerce_add_product_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-add-product.html"
)
apps_ecommerce_cart_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-cart.html"
)
apps_ecommerce_checkout_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-checkout.html"
)
apps_ecommerce_customers_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-customers.html"
)
apps_ecommerce_orders_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-orders.html"
)
apps_ecommerce_product_detail_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-product-detail.html"
)
apps_ecommerce_products_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-products.html"
)
apps_ecommerce_shops_view = AppsView.as_view(
    template_name="apps/ecommerce/ecommerce-shops.html"
)

# calendar
apps_calendar_calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")
# chat
apps_chat_chat_view = AppsView.as_view(template_name="apps/apps-chat.html")

# Email
apps_email_inbox_view = AppsView.as_view(
    template_name="apps/email/apps-email-inbox.html"
)
apps_email_read_view = AppsView.as_view(template_name="apps/email/apps-email-read.html")

# # Invoices
# apps_invoice_list_view = AppsView.as_view(
#     template_name="apps/invoices/invoice_list.html"
# )
# apps_invoice_details_view = AppsView.as_view(
#     template_name="apps/invoices/invoice_details.html"
# )

# Tasks
apps_tasks_create_view = AppsView.as_view(template_name="apps/tasks/tasks-create.html")
apps_tasks_kanban_view = AppsView.as_view(template_name="apps/tasks/tasks-kanban.html")
apps_tasks_list_view = AppsView.as_view(template_name="apps/tasks/tasks-list.html")


# Contacts
apps_contacts_usergrid_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-grid.html"
)
apps_contacts_userlist_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-list.html"
)
apps_contacts_profile_view = AppsView.as_view(
    template_name="apps/contacts/apps-contacts-profile.html"
)


# horizontal
apps_horizontal_horizontal_view = AppsView.as_view(
    template_name="apps/horizontal/horizontal.html"
)
