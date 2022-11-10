from django.shortcuts import render
from main.models import Sensor, Record
from main.forms import new_record,filter_records

def get_record(response,id):
    record = Record.objects.get(id = id)
    return render(response,"main/record.html", {"record": record})


def list_all_records(response):
    records = Record.objects.all()
    print(records)
    new_form = None
    filter_form = None
    if response.method == "POST":
        new_form = new_record(response.POST)
        filter_form = filter_records(response.POST)

        if response.POST.get("form_type") == 'new':
            if new_form.is_valid():
                date = new_form.cleaned_data["date"]
                sensor = new_form.cleaned_data["sensor"]
                value = new_form.cleaned_data["value"]
                try:
                    sensor = Sensor.objects.get(name=sensor)
                    sensor.record_set.create(date = date, sensor = sensor, value = value)
                except:
                    return render(response,"main/sensor_not_real.html", {})

        if response.POST.get("form_type") == 'filter':
            if filter_form.is_valid():
                date_0 = filter_form.cleaned_data["date_0"]
                date_1 = filter_form.cleaned_data["date_1"]
                sensor = filter_form.cleaned_data["sensor"]
                value = filter_form.cleaned_data["value"]
                boolean_value = filter_form.cleaned_data["boolean_value"]
                
                d_range = records
                name = records
                higher = records
                lower = records

                if date_0 and date_1:
                    d_range = Record.objects.filter(date__range=[date_0, date_1])
                if sensor:
                    try:
                        name = Sensor.objects.get(name=sensor).record_set.all()
                    except:
                        return render(response,"main/sensor_not_real.html", {})
                if value:
                    if boolean_value == True:
                        higher = Record.objects.filter(value__gte=value)
                    if boolean_value == False:
                        lower = Record.objects.filter(value__lte=value)
                
                records = d_range & name & higher & lower
                print(records)
    else:
        new_form = new_record()
        filter_form = filter_records()
    
        
    return render(response,"main/all_records.html", {"records": records, "new_form": new_form, "filter_form": filter_form})