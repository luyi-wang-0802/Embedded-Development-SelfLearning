import time
import ujson
import network
from config import *
from umqtt.simple import MQTTClient

def connect_to_wifi(wifi_configurations, timeout=10):
    '''
    Function to connect to Wi-Fi networks

    Parameters:
        - wifi_configurations: list of tuples, each containing Wi-Fi SSID and password
        - timeout: int, connection timeout in seconds, default is 10 seconds

    Returns:
        - None

    Exceptions:
        - Raises Exception when all Wi-Fi connections fail
    '''
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    for ssid, password in wifi_configurations:
        if not wifi.isconnected():
            wifi.active(True)
            try:
                wifi.connect(ssid, password)

                start_time = time.time()
                while not wifi.isconnected():
                    if time.time() - start_time > timeout:
                        break

                if wifi.isconnected():
                    print("Wi-Fi connected:", wifi.ifconfig())
                    return 0
                else:
                    print("Failed to connect Wi-Fi:", ssid)
                    wifi.active(False)
                    
            except OSError as e:
                print("Wi-Fi %s connection Error: %s" % (ssid, e))
                wifi.active(False)
        
        else:
            print("Wi-Fi already connected:", wifi.ifconfig())
            return 0

    raise Exception("Wi-Fi connection failed")


def connect_to_mqtt_broker(client_id, server, port=1883, username=None, password=None):
    '''
    Function to connect to MQTT broker

    Parameters:
        - client_id: str, MQTT client ID
        - server: str, MQTT broker address
        - port: int, MQTT broker port, default is 1883
        - username: str, MQTT broker username, default is None
        - password: str, MQTT broker password, default is None

    Returns:
        - MQTTClient object, connected client to MQTT broker
    '''
    client = MQTTClient(client_id, server, port, username, password)
    client.connect()
    print("Successfully connected to the server: \n%s\n" % server)
    
    client.set_callback(mqtt_callback)

    return client


def mqtt_callback(topic, msg):
    '''
    MQTT message callback function

    Parameters:
        - topic: bytes, topic of the MQTT message
        - msg: bytes, content of the MQTT message

    Returns:
        - None
    '''
    print("Received MQTT message:")
    print("Topic:", topic.decode('utf-8'))
    raw_data = ujson.loads(msg.decode('utf-8'))
    message = raw_data.get("uplink_message", {}).get("decoded_payload", {})
    print("Message:", message)
    print()


# main
connect_to_wifi(wifi_configurations)
client = connect_to_mqtt_broker(MQTT_CLIENT_ID, MQTT_SERVER, port=1883, username=MQTT_USERNAME, password=MQTT_PASSWORD)
client.subscribe(MQTT_TOPIC)
print("Successfully subscribe to the topic: \n%s\n" % MQTT_TOPIC)

# Loop and wait for receiving MQTT messages
while True:
    client.check_msg()
    time.sleep(1) 

# Disconnect MQTT connection
client.disconnect()