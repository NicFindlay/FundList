from django.urls import path

from .views import (
    pages_horizontal_layout_view,
)

app_name = "pages"

urlpatterns = [
    #  Layout
    path(
        "layout/horizontal",
        view=pages_horizontal_layout_view,
        name="pages.layout.horizontal",
    ),
]
