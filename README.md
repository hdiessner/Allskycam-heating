# Allskycam-heating
Heating for a Raspberry Pi powered device, e.g. an Allsky Cam.

The purpose of this repository is to provide a cheap and simple way to heat any device powered by a Raspberry Pi, e.g. if it is operated in cold or dewy environments. My use case is to keep dew from building up on the acrylic dome of an allsky cam - specifically this one: https://github.com/thomasjacquin/allsky

## Design principles:
- low power consumption, e.g. when the Raspberry is powered via PoE
- as few parts as possible, e.g. no extra piHATs or similar
- coming with the point above, as low cost as possible, only a 5v relay and some resistors needed
- integration in a smart home / IoT environment using MQTT

## Hardware Installation

Bill of Materials
-  1 relay 5v - e.g this one: https://amzn.to/2vl4VVr
-  6 resistors 100 Ohm
-  1 small breadboard

For assembly, simply solder the resistors in parallel onto the breadboard.
Connect the breadboard and the 5v relay to the GPIO pins:
```
PIN 2 (5V) ------ Relay VCC
PIN 4 (5V) ------ Relay NO
PIN 6 (GND) ----- Relay GND
PIN 9 (GND) ----- breadboard -
PIN 11 (GPIO17)-- Relay IN
Relay COM ------- breadboard +
```

## Software Installation on your Raspberry Pi

```sh
sudo apt-get install python-dev python-pip
sudo pip install wiringpi
sudo pip install paho-mqtt
```

Adapt allskyheating.py script to your environment.

```
MQTT Server --> enter your MQTT Server address
MQTT topics --> define the topics, e.g. /sternwarte/allskyheating
```

Copy allskyheating.py to /home/pi on your Raspberry Pi.
Copy allskyheating.service to /lib/systemd/system

```sh
sudo chmod 644 /lib/systemd/system/allskyheating.service
sudo systemctl daemon-reload
sudo systemctl enable allskyheating.service
sudo reboot
```

Now you can turn heating of your Raspberry Pi on and off using mqtt commands or have it done automatically based on time or current weather conditions.

### Example:
- Topic: /sternwarte/allskyheating
- Payload: on / off
