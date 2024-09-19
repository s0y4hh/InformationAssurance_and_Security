import random
import time

class TemperatureSensor:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def read_temperature(self):
        return random.uniform(20, 30)

class SmartThermostat:
    def __init__(self, name, target_temperature):
        self.name = name
        self.target_temperature = target_temperature
        self.current_temperature = 0
        self.is_heating = "off"  # Initialize as "off"
    
    def set_target_temperature(self, temperature):
        self.target_temperature = temperature
    
    def update_current_temperature(self, temperature):
        self.current_temperature = temperature
        self.is_heating = "on" if self.current_temperature < self.target_temperature else "off"
    
    def status(self):
        return f"Thermostat: {self.name}, Target Temperature: {self.target_temperature}°C, Current Temperature: {round(self.current_temperature, 1)}°C, Heating: {self.is_heating}"

# Create temperature sensor objects
living_room_sensor = TemperatureSensor("Living Room", "Living Room")
bedroom_sensor = TemperatureSensor("Bedroom", "Bedroom")

# Create smart thermostat object
thermostat = SmartThermostat("Smart Thermostat", 25)

# Simulation
def SimulateSmartThermostat():
    for time_step in range(10):
        # Read temperatures from sensors
        living_room_temperature = living_room_sensor.read_temperature()
        bedroom_temperature = bedroom_sensor.read_temperature()
        
        # Calculate average temperature
        average_temperature = (living_room_temperature + bedroom_temperature) / 2
        
        # Update thermostat with average temperature
        thermostat.update_current_temperature(average_temperature)
        
        # Print current time, sensor readings, and thermostat status
        print(f"""Time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
Living Room Temperature: {round(living_room_temperature, 1)}°C
Bedroom Temperature: {round(bedroom_temperature, 1)}°C
{thermostat.status()}
{"-" * 50}""")
        
        # Wait 2 seconds before next iteration
        time.sleep(2)
if __name__ == "__main__":
    SimulateSmartThermostat()
