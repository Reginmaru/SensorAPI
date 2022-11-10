from django.urls import path;

from .components import sensor,record

urlpatterns = [
    path("api/sensor/<int:id>", sensor.get_sensor, name="Sensor"),
    path("api/sensor/", sensor.list_all_sensors, name="Sensors" ),
    path("api/data/<int:id>", record.get_record, name="Record"),
    path("api/data/", record.list_all_records, name="Records" ),
]