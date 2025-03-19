import paho.mqtt.client as mqtt


# Define the callback functions for MQTT connection and message handling
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # Subscribe to the topic
        client.subscribe("contacts/excel_generated")
    else:
        print(f"Failed to connect, return code {rc}")


def on_message(client, userdata, msg):

    print(f"Excel Export Notification: {msg.payload.decode()}")


# Create an MQTT client instance
def start_mqtt_subscriber():
    """Sets up and starts the MQTT subscriber."""
    # Create an MQTT client object (now no need for client_id)
    mqtt_client = mqtt.Client()

    # Set the callbacks directly
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Connect to the MQTT broker
    mqtt_broker = "mqtt.eclipseprojects.io"
    mqtt_port = 1883
    mqtt_client.connect(mqtt_broker, mqtt_port, 60)

    # Start listening for messages indefinitely
    mqtt_client.loop_forever()


if __name__ == "__main__":
    start_mqtt_subscriber()
