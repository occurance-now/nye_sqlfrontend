from django.conf.urls import url
from mssqlFrontEnd import views
from django.urls import path, include
from .views import (
    homeView,
    parentAssetListMP,
    childAssetDataMP,
    dateRangeParentMP,
    searchChildAssetMP,
    dateRangeParentChildMP,
    chartDateRange,
    homeViewBP,
    homeViewFP,
    homeViewUniflor,
    homeViewDamping,

)

urlpatterns=[
    url(r'^home/$', homeView.as_view(), name='home-details'),
    url(r'^homeBP/$', homeViewBP.as_view(), name='home-detailsBP'),
    url(r'^homeFP/$', homeViewFP.as_view(), name='home-detailsFP'),
    url(r'^homeUniflor/$', homeViewUniflor.as_view(), name='home-detailsUniflor'),
    url(r'^homeDamping/$', homeViewDamping.as_view(), name='home-detailsDamping'),
    path('parentAssetListMP/<str:table_name>', views.parentAssetListMP, name='parent-AssetList'),#Parent asset with list of child assets over last day\\
    path('dateRangeParentMP/<str:table_name>/', views.dateRangeParentMP, name='data-RangeParent'),#Search for parent asset data over date range  xx
    path('childAssetDataMP/<str:table_name>/<str:tag_name>/', views.childAssetDataMP, name='childAsset-data'),#Child asset data from today\\\
    path('chart/data/home/press/range/<str:table_name>/<str:tag_name>/<str:q1>/<str:q2>/', views.chartDateRange, name='chart-DateRange'),
    path('dateRangeParentChildMP/<str:table_name>/<str:tag_name>/<str:q1>/<str:q2>/', views.dateRangeParentChildMP, name='dateRangeParentChild-data'),#date range of child from parent asset \\
    path('dateRangeChild/<str:table_name>/<str:tag_name>/', views.searchChildAssetMP, name='data-RangeChild'),# xx

]
