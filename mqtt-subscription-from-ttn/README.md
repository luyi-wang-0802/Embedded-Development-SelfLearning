# MQTT subscription from TTN

This code is used to subscribe to messages in a specific MQTT server and extract the content we need from it.

The message comes from TTN (The Things Network) and the processed payload is stored in decoded_payload under uplink_message, which contains information such as temperature, humidity, CO2 etc.

Since you have to be connected to the network to access the MQTT server, you can choose any WiFi around you to access the network. If you and I are not using the same WiFi, please change the WiFi configuration.

If you want to change the topic of the subscription, modify the MQTT_TOPIC variable; if you want to change the content extracted from the message, modify the message variable in the mqtt_callback function (raw_data is a dictionary format).

Ruiming Wu, 19.04.2023