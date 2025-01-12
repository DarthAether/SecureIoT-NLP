import paho.mqtt.client as mqtt
from risk_detector import detect_risks

def on_message(client, userdata, message):
    """
    Callback function that is triggered when a message is received from the MQTT broker.
    """
    rule_data = [{"description": message.payload.decode()}]
    detected_risks = detect_risks(rule_data)
    print(f"Detected risks for rule: {detected_risks}")

def monitor_rules():
    """
    Monitor IoT rule updates from the MQTT broker.
    """
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("mqtt.eclipse.org", 1883, 60)  # Using a public MQTT broker
    client.subscribe("iot/rules")
    client.loop_forever()

