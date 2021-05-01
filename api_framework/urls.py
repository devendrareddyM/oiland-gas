"""api_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
# authentication
from application_interface.authentication.autehntication import authentication
from application_interface.configurations.add_predicted_values import add_predicted_config_values
from application_interface.configurations.algo_start import update_parameter_input_status
from application_interface.configurations.get_version_list import get_version_list
from application_interface.configurations.get_versions import get_predicted_version_values
from application_interface.configurations.update_config import update_predicted_config_values
from application_interface.dash_board.coke_actual_predicted_values import get_coke_actual_predicted_values
from application_interface.dash_board.cpr_ucl_lcl import get_cpr_sor_eor
from application_interface.dash_board.frl_actual import get_furnace_run_data
from application_interface.dash_board.frl_actual_all import get_frl_actual_data
from application_interface.dash_board.frl_multi_graph import frl_multi_line_graph
from application_interface.dash_board.frl_over_view import frl_ovr_dash
from application_interface.dash_board.frl_ovr import frl_ovr_view_dash
from application_interface.dash_board.frl_view import frl_view_dash
from application_interface.dash_board.get_pre_post_rec_data import get_coke_actual_predicted_post_pre_rec_values
from application_interface.dash_board.optimised_data import get_optimized_data
from application_interface.dash_board.optimised_graph import dash_board_frl_optimised_graph
from application_interface.dash_board.optimised_multi_line_graph import dash_board_frl_optimised_multi_line_graph
from application_interface.dash_board.optimised_ovr_data import frl_optimised_ovr_view_dash
from application_interface.dash_board.optimised_run_length import frl_optimized_run_length
from application_interface.dash_board.optimized_overview import frl_optimized_ovr_dash
from application_interface.dash_board.over_view import over_view_data
from application_interface.dash_board.run_list import run_list
from application_interface.dash_board.save_reports import save_data
from application_interface.dash_board.update_predicted_values import update_predicted_values
from application_interface.dash_board.upload_csv import upload_details
from application_interface.dash_board.zone_wise import get_zone_wise_data
from application_interface.graphs.actual_yields_graph import actual_yields_graph_data
from application_interface.graphs.demo import dash_board_graph
from application_interface.graphs.frl_gph import dash_board_frl_graph
from application_interface.graphs.get_start_end_date import get_start_and_end_data
from application_interface.graphs.pie_chart import pie_chart_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', authentication, name='authentication'),
    path('dash_board/over_view', over_view_data, name='over_view_data'),
    path('dash_board/graph', dash_board_graph, name='dash_board_graph'),
    path('dash_board/update', update_predicted_values, name='update_predicted_values'),
    path('configurations/get_versions', get_predicted_version_values, name='get_predicted_version_values'),
    path('configurations/update', update_predicted_config_values, name='update_predicted_config_values'),
    path('configurations/add', add_predicted_config_values, name='add_predicted_config_values'),
    path('version/list', get_version_list, name='get_version_list'),
    path('dashboard/coke_yields', get_coke_actual_predicted_values, name='get_coke_actual_predicted_values'),
    path('dashboard/save', save_data, name='save_data'),
    path('dash_board/pie_chart', pie_chart_data, name='pie_chart_data'),
    path('dash_board/st_end_date', get_start_and_end_data, name='get_start_and_end_data'),
    path('configurations/status', update_parameter_input_status, name='update_parameter_input_status'),
    path('dashboard/pre_post/rec', get_coke_actual_predicted_post_pre_rec_values,
         name='get_coke_actual_predicted_post_pre_rec_values'),
    path('dash_board/actual_yields/graph', actual_yields_graph_data, name='actual_yields_graph_data'),
    path('dashboard/furnace/run', get_furnace_run_data),
    path('dashboard/furnace/run/all', get_frl_actual_data),
    path('dashboard/furnace/run/zone', get_zone_wise_data),
    path('dash_board/over_view/graph', dash_board_frl_graph),
    path('dashboard/furnace/sor_eor', get_cpr_sor_eor),
    path('dash_board/multi_line/graph', frl_multi_line_graph),
    path('dashboard/frl_over_view', frl_view_dash),
    path('dashboard/over_view', frl_ovr_view_dash),
    path('dashboard/run', run_list),
    path('dashboard/ovr_view', frl_ovr_dash),
    path('dashboard/optimised/over_view', frl_optimized_ovr_dash),
    path('dashboard/optimised', frl_optimised_ovr_view_dash),
    path('data/upload', upload_details),
    path('dashboard/optimised/graph', dash_board_frl_optimised_graph),
    path('dashboard/optimised/multi_line/graph', dash_board_frl_optimised_multi_line_graph),
    path('dashboard/optimised/run_length', frl_optimized_run_length),
    path('dashboard/optimised/data', get_optimized_data)
]
