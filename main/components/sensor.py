from django.shortcuts import render
from main.models import Sensor
from main.forms import new_sensor
from django.db import IntegrityError



def get_sensor(response,id):
    sensor_1 = Sensor(1,"resr","resk")
    sensor_1.save()
    sensor = Sensor.objects.get(id = id)
    return render(response,"main/sensor.html", {"sensor": sensor})

def list_all_sensors(response):
    sensors = Sensor.objects.all()
    if response.method == "POST":
        form = new_sensor(response.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            unit = form.cleaned_data["unit"]
            try:
                form_new_sensor = Sensor(name=name,unit=unit)
                form_new_sensor.save()
            except IntegrityError as e: 
                return render(response,"main/error_unique.html", {})

    else:
        form = new_sensor()

    return render(response,"main/all_sensors.html", {"sensors": sensors, "form":form})




