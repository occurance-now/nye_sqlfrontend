from django.conf.urls import url
from mssqlFrontEnd import views
from django.urls import path, include
from .views import (
    #TemperaturesListView,
    #PressureListView,
    homeView,
    homeViewBP,
    homeViewFP,
    homeViewUniflor,
    homeViewDamping,
    childAssetList,
    ChartDataHome,
    chartDataTempId,
    #chartDataTempIdRange,
    #chartDataPressId,
    #chartDataPressIdRange,

)

urlpatterns=[
    #url(r'^department$', views.departmentAPI),
    #url(r'^department/([0-9]+)$',views.departmentAPI),
    url(r'^home/$', homeView.as_view(), name='home-details'),
    url(r'^homeBP/$', homeViewBP.as_view(), name='home-detailsBP'),
    url(r'^homeFP/$', homeViewFP.as_view(), name='home-detailsFP'),
    url(r'^homeUniflor/$', homeViewUniflor.as_view(), name='home-detailsUniflor'),
    url(r'^homeDamping/$', homeViewDamping.as_view(), name='home-detailsDamping'),

    url(r'^api/chart/data/home/$', ChartDataHome.as_view()),
    path('chart/data/home/temp/<str:my_key>', views.chartDataTempId, name='chart-tempId'),

    path('childAssetList/<str:my_key>', views.childAssetList, name='child-AssetList'),
    path('dateRangeTemperature/<str:my_key>', views.searchTemperature, name='date-temp'),

    #path('homeTemp/', TemperaturesListView.as_view(), name='data-homeTemp'),

    #path('homeTemp/', TemperaturesListView.as_view(), name='data-homeTemp'),



]

'''
path('chart/data/home/temp/range/<str:my_key>/<str:q1>/<str:q2>', views.chartDataTempIdRange, name='chart-tempIdRange'),

path('chart/data/home/press/<str:my_key>', views.chartDataPressId, name='chart-pressId'),
path('chart/data/home/press/range/<str:my_key>/<str:q1>/<str:q2>', views.chartDataPressIdRange, name='chart-pressIdRange'),

path('homeTemp/', TemperaturesListView.as_view(), name='data-homeTemp'),
path('stored_procTemperature/<str:my_key>', views.stored_procTemperature, name='temperature-detail'),
path('homePress/', PressureListView.as_view(), name='data-homePress'),

path('stored_procPressure/<str:my_key>', views.stored_procPressure, name='pressure-detail'),
path('dateRangePressure/<str:my_key>', views.searchPressure, name='date-press'),
'''
