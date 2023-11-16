## Useful links

[Soil moisture sensor tutorial](https://lastminuteengineers.com/soil-moisture-sensor-arduino-tutorial/)
[Temperature and humidity sensor tutorial](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor/python-circuitpython)
[Passive infrared sensor tutorial](https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio)
[Soil moisture sensor module](https://einstronic.com/product/soil-moisture-level-sensor-module/)
[Soil moisture sensor analog tutorial](https://maker.pro/raspberry-pi/tutorial/interfacing-soil-moisture-sensor-with-raspberry-pi)
[Lux sensor tutorial](https://www.adafruit.com/product/5378)



[grafana docker image](https://hub.docker.com/r/grafana/grafana-arm32v7-linux) for ARM 32 bit v7

sudo pip3 install adafruit-circuitpython-sht4x
sudo pip3 install adafruit-circuitpython-veml7700

mkdir DataVisual
cd DataVisual
sudo nano docker-compose.yml
sudo docker compose up -d

sudo docker exec -it influxdb influx
CREATE DATABASE sensor_data

cd ../Documents
nano sensors.py


sudo nano /etc/systemd/system/dataCollection.service
sudo systemctl daemon-reload
sudo systemctl start dataCollection
sudo systemctl status dataCollection
sudo systemctl enable dataCollection

