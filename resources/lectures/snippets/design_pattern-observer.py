"""
Observer pattern example.
"""
class SensorArray:
    def __init__(self):
        self._sensors = []

    def register_sensor(self, sensor):
        self._sensors.append(sensor)

    def set_precision(self, precision):
        for sensor in self._sensors:
            sensor.set_precision(precision)


class Sensor:
    def __init__(self, name, sensor_array):
        self._name = name
        self._precision = "Low"
        sensor_array.register_sensor(self)

    def set_precision(self, precision):
        self._precision = precision
        print("{}: precision is set to {}".format(
            self._name, self._precision))


sensor_array = SensorArray()
sensor1 = Sensor("S1", sensor_array)
sensor2 = Sensor("S2", sensor_array)

sensor_array.set_precision("High")
sensor_array.set_precision("Low")
