from django.conf.urls import url
from mssqlFrontEnd import views
from django.urls import path, include
from .views import (
    TemperaturesListView,
    PressureListView,
    get_data,
    homeView,
    ChartDataHome,
    ChartDataTemperatureHome,


)
urlpatterns=[
    url(r'^department$', views.departmentAPI),
    url(r'^department/([0-9]+)$',views.departmentAPI),

    url(r'^api/data/$', views.get_data, name='api-data'),

    url(r'^home/$', homeView.as_view(), name='home-details'),
    url(r'^api/chart/data/home/$', ChartDataHome.as_view()),
    url(r'^api/chart/data/home/temp/$', ChartDataTemperatureHome.as_view()),

    
    path('homeTemp/', TemperaturesListView.as_view(), name='data-homeTemp'),
    path('stored_procTemperature/<str:my_key>', views.stored_procTemperature, name='temperature-detail'),
    path('dateRangeTemperature/<str:my_key>', views.searchTemperature, name='date-temp'),
    path('homePress/', PressureListView.as_view(), name='data-homePress'),
    path('stored_procPressure/<str:my_key>', views.stored_procPressure, name='pressure-detail'),
    path('dateRangePressure/<str:my_key>', views.searchPressure, name='date-press'),



]
