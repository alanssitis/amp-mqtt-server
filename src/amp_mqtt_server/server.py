import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


def publish_count(topic, client):
    client.publish(topic, "hello")


def handle_command(cmd, client):
    if cmd == "help":
        print("help msgs not implemented yet")
    elif cmd.startswith("reg "):
        topic = cmd.split()[1]
        publish_count(topic, client)
    else:
        print("write `help` to get help")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost")
    client.loop_start()

    while True:
        try:
            cmd = input()
            handle_command(cmd, client)
        except KeyboardInterrupt:
            client.loop_stop()
            print("stopped client loop")
            break

    print("exit")
