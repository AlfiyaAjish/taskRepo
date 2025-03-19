import paho.mqtt.client as mqtt



def publish_mqtt_message():
    """Publishes a message to MQTT when the Excel file is generated."""
    try:
        mqtt_client = mqtt.Client()
        mqtt_client.connect("mqtt.eclipseprojects.io", 1883, 60)
        mqtt_client.publish("contacts/excel_generated", "Excel file has been generated successfully.")
        mqtt_client.disconnect()
    except Exception as e:
        print(f"there is some error {e}")