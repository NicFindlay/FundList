from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()
# class ElementsView(LoginRequiredMixin, TemplateView):
class ElementsView(TemplateView):
    pass


# Bootstrap
components_bootstrap_alerts_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-alerts.html"
)
components_bootstrap_buttons_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-buttons.html"
)
components_bootstrap_cards_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-cards.html"
)
components_bootstrap_carousel_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-carousel.html"
)
components_bootstrap_dropdowns_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-dropdowns.html"
)
components_bootstrap_grid_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-grid.html"
)
components_bootstrap_images_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-images.html"
)
components_bootstrap_modals_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-modals.html"
)
components_bootstrap_offcanvas_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-offcanvas.html"
)
components_bootstrap_progressbars_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-progressbars.html"
)
components_bootstrap_placeholders_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-placeholders.html"
)
components_bootstrap_tabs_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-tabs-accordions.html"
)
components_bootstrap_typography_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-typography.html"
)
components_bootstrap_video_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-video.html"
)
components_bootstrap_general_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-general.html"
)
components_bootstrap_colors_view = ElementsView.as_view(
    template_name="components/bootstrap/ui-colors.html"
)

# Extended
components_extended_lightbox_view = ElementsView.as_view(
    template_name="components/extended/extended-lightbox.html"
)
components_extended_rangeslider_view = ElementsView.as_view(
    template_name="components/extended/extended-rangeslider.html"
)
components_extended_sweetalert_view = ElementsView.as_view(
    template_name="components/extended/extended-sweet-alert.html"
)
components_extended_sessiontimeout_view = ElementsView.as_view(
    template_name="components/extended/extended-session-timeout.html"
)
components_extended_rating_view = ElementsView.as_view(
    template_name="components/extended/extended-rating.html"
)
components_extended_notifications_view = ElementsView.as_view(
    template_name="components/extended/extended-notifications.html"
)

# Forms
components_forms_basic_elements_view = ElementsView.as_view(
    template_name="components/forms/form-elements.html"
)
components_forms_validation_view = ElementsView.as_view(
    template_name="components/forms/form-validation.html"
)
components_forms_advanced_plugins_view = ElementsView.as_view(
    template_name="components/forms/form-advanced.html"
)
components_forms_editors_view = ElementsView.as_view(
    template_name="components/forms/form-editors.html"
)
components_forms_fileupload_view = ElementsView.as_view(
    template_name="components/forms/form-uploads.html"
)
components_forms_wizard_view = ElementsView.as_view(
    template_name="components/forms/form-wizard.html"
)
components_forms_mask_view = ElementsView.as_view(
    template_name="components/forms/form-mask.html"
)

# Tables
components_tables_bootstrap_basic_view = ElementsView.as_view(
    template_name="components/tables/tables-basic.html"
)
components_tables_datatables_view = ElementsView.as_view(
    template_name="components/tables/tables-datatable.html"
)
components_tables_responsive_tables_view = ElementsView.as_view(
    template_name="components/tables/tables-responsive.html"
)
components_tables_editable_tables_view = ElementsView.as_view(
    template_name="components/tables/tables-editable.html"
)

# Charts
components_charts_apexcharts_view = ElementsView.as_view(
    template_name="components/charts/charts-apex.html"
)
components_charts_echarts_view = ElementsView.as_view(
    template_name="components/charts/charts-echart.html"
)
components_charts_chartjs_view = ElementsView.as_view(
    template_name="components/charts/charts-chartjs.html"
)
components_charts_jqueryknob_view = ElementsView.as_view(
    template_name="components/charts/charts-knob.html"
)
components_charts_sparkline_view = ElementsView.as_view(
    template_name="components/charts/charts-sparkline.html"
)

# Icons
components_icons_boxicons_view = ElementsView.as_view(
    template_name="components/icons/icons-boxicons.html"
)
components_icons_materialdesign_view = ElementsView.as_view(
    template_name="components/icons/icons-materialdesign.html"
)
components_icons_dripicons_view = ElementsView.as_view(
    template_name="components/icons/icons-dripicons.html"
)
components_icons_fontawesome_view = ElementsView.as_view(
    template_name="components/icons/icons-fontawesome.html"
)
components_icons_feather_view = ElementsView.as_view(
    template_name="components/icons/icons-feather.html"
)

# Maps
components_maps_googlemaps_view = ElementsView.as_view(
    template_name="components/maps/maps-google.html"
)
components_maps_vectormaps_view = ElementsView.as_view(
    template_name="components/maps/maps-vector.html"
)
components_maps_leaflet_view = ElementsView.as_view(
    template_name="components/maps/maps-leaflet.html"
)
