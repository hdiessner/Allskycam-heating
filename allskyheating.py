import time
import wiringpi
import paho.mqtt.client as mqtt

heating_state = False

def setup():
   wiringpi.wiringPiSetup()
   wiringpi.pinMode(0,  1) # GPIO17 - PIN11

def short(pin):
    switch_on(pin)
    time.sleep(0.5)
    switch_off(pin)

def switch_on(pin):
    wiringpi.digitalWrite(pin, 1)

def switch_off(pin):
    wiringpi.digitalWrite(pin, 0)

def on_connect(self, client, userdata, rc):
    mqclient.subscribe("sternwarte/allskyheating/#")
    
def on_message(client, userdata, msg):
    m = msg.topic.split("/")
    global heating_state

    if m[1] == "allskyheating":

        if msg.payload == "on":

            if not heating_state:
                switch_on(0)
            
            heating_state = True

        if msg.payload == "off":
        
            if heating_state:
                switch_off(0)

            heating_state = False


if __name__ == "__main__":
    setup()
    mqclient = mqtt.Client(clean_session=True)
    mqclient.connect("192.168.2.5", 1883, 60)
    mqclient.on_connect = on_connect
    mqclient.on_message = on_message
    mqclient.loop_forever()

