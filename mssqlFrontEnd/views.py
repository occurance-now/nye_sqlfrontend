from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.core.paginator import Paginator
from mssqlFrontEnd.models import FT01, GA05, GA29, KT09, KT14, KT15, KT19, KT22
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
import datetime
from datetime import date

User = get_user_model()

'''
Home View returns list of parent asssets per production area
'''
class homeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/home.html', {})

class homeViewBP(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/homeBP.html', {})

class homeViewFP(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/homeFP.html', {})

class homeViewUniflor(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/homeUniflor.html', {})

class homeViewDamping(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/homeDamping.html', {})


#############################################
###### START MIDDLE PRODUCTION AREA #########
#############################################

'''
Return list of child assets for selected parent asset Repeat below for other production areas.
'''
@login_required
def parentAssetListMP(request, table_name):
    try:
        if table_name == 'KT09':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT09 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'KT14':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT14 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'KT15':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT15 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'KT19':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT19 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'KT22':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT22 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'GA05':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM GA05 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'GA29':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM GA29 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        elif table_name == 'FT01':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM FT01 WHERE cast(RecordTime as Date) = cast(getdate() as Date) ORDER BY RecordTime DESC;")
        else:
            print('not a database')

        result = cursor.fetchall()
        paginator = Paginator(result, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'parentAsset/assetId.html', {'result': page_obj, 'db': table_name})
    finally:
        cursor.close()

'''
Returns data on specific child asset
'''
@login_required
def childAssetDataMP(request, table_name, tag_name):
    try:
        if table_name == 'KT09':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT09 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'KT14':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT14 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'KT15':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT15 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'KT19':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT19 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'KT22':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT22 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'GA05':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM GA05 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'GA29':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM GA29 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        elif table_name == 'FT01':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM FT01 WHERE cast(RecordTime as Date) = cast(getdate() as Date) and TagName = %s ORDER BY RecordTime DESC;",[tag_name])
        else:
            print('not a database')

        result = cursor.fetchall()
        paginator = Paginator(result, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        today = datetime.datetime.now()
        today_date = date.today()
        today_morning = datetime.datetime.combine(today_date, datetime.datetime.min.time())
        q1 = today_morning.strftime("%Y-%m-%dT%H:%M:%S")
        q2 = today.strftime("%Y-%m-%dT%H:%M:%S")


        return render(request, 'childAsset/assetDataMP.html', {'result': page_obj, 'q1': q1, 'q2': q2, 'db': table_name})
    finally:
        cursor.close()

'''
Search Parent Asset for data in date range
'''
@login_required
def dateRangeParentMP(request, table_name):
    error = False
    if 'q1' and 'q2'in request.GET:
        q1 = request.GET['q1']
        q2 = request.GET['q2']
        if not q1:
            error = True
        elif not q2:
            error = True
        else:
            if table_name == 'KT09':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT09 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'KT14':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT14 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'KT15':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT15 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'KT19':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT19 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'KT22':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT22 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'GA05':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM GA05 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'GA29':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM GA29 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            elif table_name == 'FT01':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM FT01 WHERE RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[q1, q2])
            else:

                print('not a database')
            result = cursor.fetchall()
            paginator = Paginator(result, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)


            return render(request, 'parentAsset/searchResultParent.html', {'result': page_obj, 'db': table_name, 'q1': q1, 'q2': q2,})
    return render(request, 'parentAsset/assetId.html', {'error': error})

'''
Retrieve data for child asset from parent date range
'''
@login_required
def dateRangeParentChildMP(request, table_name, tag_name, q1, q2):
    try:
        if table_name == 'KT09':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT09 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'KT14':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT14 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'KT15':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT15 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'KT19':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT19 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'KT22':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM KT22 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'GA05':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM GA05 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'GA29':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM GA29 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        elif table_name == 'FT01':
            cursor = connection.cursor()
            cursor.execute("SELECT TOP (5) * FROM FT01 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
        else:
            print('not a database')
        result = cursor.fetchall()
        paginator = Paginator(result, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'childAsset/searchResultChild.html', {'result': page_obj, 'q1': q1, 'q2': q2, 'db': table_name})
    finally:
        cursor.close()

'''
Search data range from child asset
'''
@login_required
def searchChildAssetMP(request, table_name, tag_name):
    error = False
    if 'q1' and 'q2'in request.GET:
        q1 = request.GET['q1']
        q2 = request.GET['q2']
        if not q1:
            error = True
        elif not q2:
            error = True
        else:
            if table_name == 'KT09':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT09 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'KT14':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT14 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'KT15':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT15 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'KT19':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT19 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'KT22':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM KT22 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'GA05':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM GA05 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'GA29':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM GA29 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            elif table_name == 'FT01':
                cursor = connection.cursor()
                cursor.execute("SELECT TOP (5) * FROM FT01 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s ORDER BY RecordTime DESC;",[tag_name, q1, q2])
            else:
                print('not a database')


            result = cursor.fetchall()
            paginator = Paginator(result, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'childAsset/searchResultChild.html', {'result': page_obj, 'db': table_name, 'q1': q1, 'q2': q2})
    return render(request, 'parentAsset/assetId.html', {'error': error})


'''
Render Chart Data
'''
@login_required
def chartDateRange(request, table_name, tag_name, q1, q2, *args, **kwargs):

    if table_name == 'KT09':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM KT09 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM KT09  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'KT14':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM KT14 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM KT14  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'KT15':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM KT15 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM KT15  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'KT19':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM KT19 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM KT19  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'KT22':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM KT22 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM KT22  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'GA05':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM GA05 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM GA05  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'GA29':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM GA29 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM GA29  WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    elif table_name == 'FT01':
        cursor = connection.cursor()
        cursor.execute("SELECT TOP (5) * FROM FT01 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s;",[tag_name, q1, q2])
        result = cursor.fetchall()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(TagValue), AVG(TagValue), MAX(TagValue) FROM FT01 WHERE TagName = %s AND RecordTime > %s AND RecordTime < %s",[tag_name, q1, q2])
        dataRange = cursor.fetchall()
    else:
        print('not a database')

    dataRangeX = ['Minimum', 'Average', 'Maximum']
    rangeValues = []
    for i in dataRange:
        for x in i:
            rangeValues.append(x)

    temp_values = []
    date_values = []
    for list in result:
        temp_values.append(list[3])
    for list in result:
        date_values.append(list[4])
    print(date_values)
    print(temp_values)
    data = {
        'x': date_values,
        'y': temp_values,
        'x2': dataRangeX,
        'y2': rangeValues,
    }

    return JsonResponse(data)









'''

#from rest_framework.views import APIView
#from rest_framework.response import Response
#from mssqlFrontEnd.serializers import DepartmentSerializer, EmployeeSerializer
#from django.contrib import messages
@login_required
def stored_procPressure(request, my_key):
    try:
        cursor = connection.cursor()
        #cursor.execute(procedure)
        cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_pressure] WHERE PressureName = %s ORDER BY PressureTimeStamp DESC;",[my_key])
        result = cursor.fetchall()
        paginator = Paginator(result, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'pressure/pressureId.html', {'result': page_obj})
    finally:
        cursor.close()

@login_required
def searchPressure(request, my_key):
    error = False
    if 'q1' and 'q2'in request.GET:
        q1 = request.GET['q1']
        q2 = request.GET['q2']

        if not q1:
            error = True
        elif not q2:
            error = True
        else:
            cursor = connection.cursor()
            #cursor.execute(procedure)
            cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_pressure] \
             WHERE PressureName = %s AND PressureTimeStamp > %s AND PressureTimeStamp < %s ORDER BY PressureTimeStamp DESC;",[my_key, q1, q2])
            result = cursor.fetchall()
            paginator = Paginator(result, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'pressure/search_results_pressure.html', {'result': page_obj, 'q1': q1, 'q2': q2})
    return render(request, 'pressure/pressureId.html', {'error': error})
class ChartDataHome(LoginRequiredMixin, APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        tempId_count = Temperatures.objects.values_list('TemperatureName').distinct().count()
        pressId_count = Pressure.objects.values_list('PressureName').distinct().count()
        ## ADD PUMP data
        ## ADD LEVEL data
        default_items = [tempId_count, pressId_count, 14, 5]
        labels = ['Temperature', 'Pressure', 'Motors', 'Level']
        data = {
            'labels': labels,
            'default_items': default_items,
        }
        return Response(data)


CRUD responses


# Create your views here.
@csrf_exempt
def departmentAPI(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)

    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepertmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Updated department Successfully',safe=False)
        return JsonResponse('Failed to Add', safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepertmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@login_required
def chartDataTempId(request, my_key, *args, **kwargs):

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_temperatures] WHERE TemperatureName = %s ORDER BY TemperatureTimeStamp DESC;",[my_key])
    result = cursor.fetchall()

    cursor = connection.cursor()
    cursor.execute("SELECT AVG(TemperatureValue), MIN(TemperatureValue), MAX(TemperatureValue) FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_temperatures]  WHERE TemperatureName = %s;",[my_key])
    dataRange = cursor.fetchall()
    dataRangeX = ['Minimum', 'Average', 'Maximum']
    rangeValues = []
    for i in dataRange:
        for x in i:
            rangeValues.append(x)

    temp_values = []
    date_values = []
    for list in result:
        temp_values.append(list[3])
    for list in result:
        date_values.append(list[4])

    data = {
        'x': date_values,
        'y': temp_values,
        'x2': dataRangeX,
        'y2': rangeValues,
    }

    return JsonResponse(data)




@login_required
def chartDataPressId(request, my_key, *args, **kwargs):

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_pressure] WHERE PressureName = %s ORDER BY PressureTimeStamp ASC;",[my_key])
    result = cursor.fetchall()

    cursor = connection.cursor()
    cursor.execute("SELECT AVG(PressureValue), MIN(PressureValue), MAX(PressureValue) FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_pressure]  WHERE PressureName = %s;",[my_key])
    dataRange = cursor.fetchall()
    dataRangeX = ['Minimum', 'Average', 'Maximum']
    rangeValues = []

    for i in dataRange:
        for x in i:
            rangeValues.append(x)

    temp_values = []
    date_values = []
    for list in result:
        temp_values.append(list[3])
    for list in result:
        date_values.append(list[4])
    data = {
        'x': date_values,
        'y': temp_values,
        'x2': dataRangeX,
        'y2': rangeValues,
    }

    return JsonResponse(data)


@login_required
def chartDataPressIdRange(request, my_key, q1, q2, *args, **kwargs):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_pressure] \
     WHERE PressureName = %s AND PressureTimeStamp > %s AND PressureTimeStamp < %s ORDER BY PressureTimeStamp DESC;",[my_key, q1, q2])
    result = cursor.fetchall()

    cursor = connection.cursor()
    cursor.execute("SELECT AVG(PressureValue), MIN(PressureValue), MAX(PressureValue) FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_pressure]  WHERE PressureName = %s AND PressureTimeStamp > %s AND PressureTimeStamp < %s",[my_key, q1, q2])
    dataRange = cursor.fetchall()
    dataRangeX = ['Minimum', 'Average', 'Maximum']
    rangeValues = []
    for i in dataRange:
        for x in i:
            rangeValues.append(x)

    temp_values = []
    date_values = []
    for list in result:
        temp_values.append(list[3])
    for list in result:
        date_values.append(list[4])

    data = {
        'x': date_values,
        'y': temp_values,
        'x2': dataRangeX,
        'y2': rangeValues,
    }

    return JsonResponse(data)

class TemperatureListView(LoginRequiredMixin, ListView):
    model = Temperatures
    template_name = 'data/homeTemp.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'temperatures'
    ordering = ['-TemperatureTimeStamp']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TemperaturesListView, self).get_context_data(**kwargs)
        context['temp_name_list'] = Temperatures.objects.order_by('TemperatureName')
        return context
'''
