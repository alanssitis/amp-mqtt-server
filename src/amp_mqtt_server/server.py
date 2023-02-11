import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_message(client, userdata, msg):
    print(msg.payload.decode())

def main():
    if len(sys.argv) == 2:
        topic = sys.argv[1]
    else:
        topic = "test"

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost")
    client.loop_start()

    while True:
        try:
            val = input()
            client.publish(topic, val)

        except KeyboardInterrupt:
            client.loop_stop()
            print("stopped client loop")
            break

    print("exit")
