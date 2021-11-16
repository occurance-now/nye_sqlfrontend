from django.db import models


# Create your models here.

class DumbyTable(models.Model):
    id = models.IntegerField(primary_key=True)
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dumby_Table'


class FT01(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FT01'
        verbose_name_plural = 'FT01'


class GA05(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GA05'
        verbose_name_plural = 'GA05'


class GA29(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GA29'
        verbose_name_plural = 'GA29'


class KT09(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KT09'
        verbose_name_plural = 'KT09'


class KT14(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KT14'
        verbose_name_plural = 'FT14'


class KT15(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KT15'
        verbose_name_plural = 'KT15'


class KT19(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KT19'
        verbose_name_plural = 'KT19'


class KT22(models.Model):
    tagname = models.CharField(db_column='TagName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    numericid = models.IntegerField(db_column='NumericID', blank=True, null=True)  # Field name made lowercase.
    tagvalue = models.FloatField(db_column='TagValue', blank=True, null=True)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KT22'
        verbose_name_plural = 'KT22'


class Keptest1(models.Model):
    temperature = models.IntegerField(db_column='Temperature')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KepTest1'
'''

class Temperatures(models.Model):
    id = models.AutoField(primary_key=True)
    TemperatureName = models.CharField(max_length=500)
    TemperatureNumericID = models.IntegerField()
    TemperatureValue = models.IntegerField()
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
    PressureValue = models.IntegerField()
    PressureTimeStamp = models.DateTimeField()
    PressureQuality = models.IntegerField()

    def __str__(self):
        return self.PressureName

    def get_absolute_url(self):
        return reverse('pressure-detail', kwargs={'pk': self.PressureName})
'''
