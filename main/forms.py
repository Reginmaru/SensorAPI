from django import forms
from main.models import Sensor

class new_sensor(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    unit = forms.CharField(label="Unit",max_length = 20)

class new_record(forms.Form):
    date = forms.DateTimeField(required=False)
    sensor = forms.CharField(label="Sensor Name", max_length=200,required=False)
    value = forms.FloatField(required=False)

class filter_records(forms.Form):
    date_0 = forms.DateTimeField(label="Start datetime.",required=False)
    date_1 = forms.DateTimeField(label="End datetime.",required=False)
    sensor = forms.CharField(label="Sensor Name", max_length=200,required=False)
    boolean_value = forms.BooleanField(label="Tick for above/ Don't tick for below.", required=False)
    value = forms.FloatField(label="Value",required=False)
    