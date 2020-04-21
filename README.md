# Allskycam-heating
Heating for a Raspberry Pi powered device, e.g. an Allsky Cam.

The purpose of this repository is to provide a cheap and simple way to heat any device powered by a Raspberry Pi, e.g. if it is operated in cold or dewy environments. My use case is to keep dew from building up on the acrylic dome of an allsky cam - specifically this one: https://github.com/thomasjacquin/allsky

## Design principles:
- low power consumption, e.g. when the Raspberry is powered via PoE
- as few parts as possible, e.g. no extra piHATs or similar
- coming with the point above, as low cost as possible, only a 5v relay and some resistors needed
- integration into smart home / IoT environment using MQTT

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

For more clarity, some schematics of the wiring:
![Raspberry Pi](https://github.com/hdiessner/Allskycam-heating/blob/master/RelaisWiring.png "Wiring of Relais")

Cable-saving version of wiring, with only one 5V wire running from Raspberry to Relais Board (daisy-chaining the 5V wire from "Relay NO" to "Relay VCC"):
![Raspberry Pi](https://github.com/hdiessner/Allskycam-heating/blob/master/RelaisWiringCableSave.png "Wiring of Relais with one cable for 5V from Raspberry to Relay board")

## Software Installation on your Raspberry Pi

```sh
sudo apt-get install python-dev python-pip
sudo pip install wiringpi
sudo pip install paho-mqtt
```

Adapt allskyheating.py script to your environment.

```
MQTT Server --> enter your MQTT Server address (line 49)
MQTT topics --> define the topics (lines 23, 29), e.g. /sternwarte/allskyheating/#
MQTT payloads --> define payload (lines 31, 38), e.g. "on" "off"
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

### Pictures:
![Raspberry Pi](https://github.com/hdiessner/Allskycam-heating/blob/master/Raspi.jpg "Raspberry Pi")

![Relay](https://github.com/hdiessner/Allskycam-heating/blob/master/Relay.jpg "Relay")

![Relay and Resistors](https://github.com/hdiessner/Allskycam-heating/blob/master/Relay_Resistors.jpg "Relay and Resistors")

### Comparison before and after:
On Youtube, you can see the effect of this heating.
The first video is a timelapse of the night from February 6th-7th, 2020 with no heating:
https://youtu.be/Hbvj66kT7Wo 

In the second video, the heating is turned on during the next night (Feb 7th-8th, 2020), both nights had similar conditions with temperatures below 0°C (minimum: -5°C).
https://youtu.be/YsjeaSNKSf8 
