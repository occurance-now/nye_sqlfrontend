from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.core.paginator import Paginator
from mssqlFrontEnd.models import Departments, Employees, Temperatures, Pressure
from mssqlFrontEnd.serializers import DepartmentSerializer, EmployeeSerializer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,

)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

User = get_user_model()

'''
Data Views
'''
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
def chartDataTempIdRange(request, my_key, q1, q2, *args, **kwargs):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_temperatures] \
     WHERE TemperatureName = %s AND TemperatureTimeStamp > %s AND TemperatureTimeStamp < %s ORDER BY TemperatureTimeStamp ASC;",[my_key, q1, q2])
    result = cursor.fetchall()

    cursor = connection.cursor()
    cursor.execute("SELECT AVG(TemperatureValue), MIN(TemperatureValue), MAX(TemperatureValue) FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_temperatures]  WHERE TemperatureName = %s AND TemperatureTimeStamp > %s AND TemperatureTimeStamp < %s",[my_key, q1, q2])
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


'''
Home View
'''
class homeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/home.html', {})

'''
Temperature Views
'''
class TemperaturesListView(LoginRequiredMixin, ListView):
    model = Temperatures
    template_name = 'data/homeTemp.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'temperatures'
    ordering = ['-TemperatureTimeStamp']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TemperaturesListView, self).get_context_data(**kwargs)
        context['temp_name_list'] = Temperatures.objects.order_by('TemperatureName')
        return context


@login_required
def searchTemperature(request, my_key):
    error = False
    print('search def')
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
            cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_temperatures] \
             WHERE TemperatureName = %s AND TemperatureTimeStamp > %s AND TemperatureTimeStamp < %s ORDER BY TemperatureTimeStamp DESC;",[my_key, q1, q2])
            result = cursor.fetchall()
            paginator = Paginator(result, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'temperatures/search_results.html', {'result': page_obj, 'q1': q1, 'q2': q2})
    return render(request, 'temperatures/tempId.html', {'error': error})


@login_required
def stored_procTemperature(request, my_key):
    try:
        cursor = connection.cursor()
        #cursor.execute(procedure)
        cursor.execute("SELECT * FROM [DJANGO_MSSQL].[dbo].[mssqlFrontEnd_temperatures] WHERE TemperatureName = %s ORDER BY TemperatureTimeStamp DESC;",[my_key])
        result = cursor.fetchall()
        paginator = Paginator(result, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'temperatures/tempId.html', {'result': page_obj})
    finally:
        cursor.close()


'''
Pressure
'''

class PressureListView(LoginRequiredMixin, ListView):
    model = Pressure
    template_name = 'data/homePress.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pressure'
    ordering = ['-PressureTimeStamp']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PressureListView, self).get_context_data(**kwargs)
        context['pressure_name_list'] = Pressure.objects.order_by('PressureName')
        return context

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

'''
CRUD responses
'''
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
