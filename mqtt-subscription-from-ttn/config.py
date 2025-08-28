import machine
import ubinascii

# Wi-Fi connection information
'''
The first item of this tuple is the WiFi name and the second item is the WiFi password.
Instead of deleting the old WiFi configuration when configuring a new WiFi,
just add the new WiFi configuration under this tuple
so that when you return to the past environment and try to connect, you can avoid reconfiguration

The connect_to_wifi function in main will try to connect to each combination in this tuple until the connection succeeds or all connections fail
'''
wifi_configurations = [
    ("EmRoLab-ng", "#HTWdS5307%_"),
    ("second_wifi_ssid", "second_wifi_password"),
    ("third_wifi_ssid", "third_wifi_password"),
]

# MQTT broker information
MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
MQTT_SERVER = "eu1.cloud.thethings.network"
MQTT_PORT = 1883
MQTT_USERNAME = "htw-saar-ersco2@ttn"
MQTT_PASSWORD = "NNSXS.NX66ENUCJRFGTQNEKIZXAWDQ2SMQVRICFCKEOCY.UTUZ4HOWJZELV5Z3VK43BAJ33B23UHFHYIBAKYD2MCDSGXVWH4LA"

MQTT_TOPIC = "v3/htw-saar-ersco2@ttn/devices/#"