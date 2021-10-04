from django.db import models


# Create your models here.

class Departments(models.Model):
    DepertmentId = models.AutoField(primary_key=True)
    DepartmendName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class Temperatures(models.Model):
    id = models.AutoField(primary_key=True)
    TemperatureName = models.CharField(max_length=500)
    TemperatureNumericID = models.IntegerField()
    TemperatureValue = models.CharField(max_length=500)
    TemperatureTimeStamp = models.DateTimeField()
    TemperatureQuality = models.IntegerField()

    def __str__(self):
        return self.TemepratureName

    def get_absolute_url(self):
        return reverse('temperature-detail', kwargs={'pk': self.TemperatureName})

class Pressure(models.Model):
    id = models.AutoField(primary_key=True)
    PressureName = models.CharField(max_length=500)
    PressureNumericID = models.IntegerField()
    PressureValue = models.CharField(max_length=500)
    PressureTimeStamp = models.DateTimeField()
    PressureQuality = models.IntegerField()

    def __str__(self):
        return self.PressureName

    def get_absolute_url(self):
        return reverse('pressure-detail', kwargs={'pk': self.PressureName})
