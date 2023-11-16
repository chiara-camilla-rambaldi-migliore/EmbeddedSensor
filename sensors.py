import time
import board
import adafruit_sht4x
import adafruit_veml7700
import digitalio
import requests

i2c = board.I2C()   # uses board.SCL and board.SDA


sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION


#veml7700 = adafruit_veml7700.VEML7700(i2c)

PIR_pin = board.D17 #GPIO17
pir_sensor = digitalio.DigitalInOut(PIR_pin)
pir_sensor.direction = digitalio.Direction.INPUT

soil_pin = board.D18 #GPIO18
soil_sensor = digitalio.DigitalInOut(soil_pin)
soil_sensor.direction = digitalio.Direction.INPUT


while True:
    
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    #print("Ambient light:", veml7700.light)
    print("PIR: ", pir_sensor.value)
    print("Soil: ", soil_sensor.value)
    
    db_name = "sensor_data"
    url = f'http://localhost:8086/write?db={db_name}&precision=s'
    fields = [
        f"humidity={relative_humidity}",
        f"temperature={temperature}",
        #f"lux={veml7700.light}",
        f"soil={1 if soil_sensor.value else 0}",
        f"pir={1 if pir_sensor.value else 0}"
    ]
    data = f'rasp_3_b_plus {",".join(fields)}'

    headers = {'Content-Type': 'application/octet-stream'}

    response = requests.post(url, headers=headers, data=data)

    # Print the response status code
    print(f'Status Code: {response.status_code}')

    # Print the response content
    print('Response Content:')
    print(response.text)
    
		
    time.sleep(10)
