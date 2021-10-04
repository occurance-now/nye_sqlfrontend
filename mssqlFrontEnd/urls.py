from django.conf.urls import url
from mssqlFrontEnd import views
from django.urls import path, include
from .views import (
    TemperaturesListView,
    PressureListView,
    homeView,
    ChartDataHome,
    chartDataTempId,
    chartDataTempIdRange,
    chartDataPressId,
    chartDataPressIdRange,

)

urlpatterns=[
    url(r'^department$', views.departmentAPI),
    url(r'^department/([0-9]+)$',views.departmentAPI),
    url(r'^home/$', homeView.as_view(), name='home-details'),

    #Render Charts
    url(r'^api/chart/data/home/$', ChartDataHome.as_view()),
    path('chart/data/home/temp/<str:my_key>', views.chartDataTempId, name='chart-tempId'),
    path('chart/data/home/temp/range/<str:my_key>/<str:q1>/<str:q2>', views.chartDataTempIdRange, name='chart-tempIdRange'),

    path('chart/data/home/press/<str:my_key>', views.chartDataPressId, name='chart-pressId'),
    path('chart/data/home/press/range/<str:my_key>/<str:q1>/<str:q2>', views.chartDataPressIdRange, name='chart-pressIdRange'),

    path('homeTemp/', TemperaturesListView.as_view(), name='data-homeTemp'),
    path('stored_procTemperature/<str:my_key>', views.stored_procTemperature, name='temperature-detail'),
    path('dateRangeTemperature/<str:my_key>', views.searchTemperature, name='date-temp'),
    path('homePress/', PressureListView.as_view(), name='data-homePress'),

    path('stored_procPressure/<str:my_key>', views.stored_procPressure, name='pressure-detail'),
    path('dateRangePressure/<str:my_key>', views.searchPressure, name='date-press'),



]
