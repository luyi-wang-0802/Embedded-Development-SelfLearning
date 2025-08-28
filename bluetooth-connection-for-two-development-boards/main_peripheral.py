from machine import UART
from BLE_Peripheral import BLE_Peripheral
import time
import bluetooth
import getGPS

ble = bluetooth.BLE()
lora_32 = BLE_Peripheral(ble, name="Lora_32")

UART_TX = 17
UART_RX = 36

gpsModule = UART(2, baudrate=9600, tx=UART_TX, rx=UART_RX)
print(gpsModule)

def RX_Roport(data):
    print("RX", data.decode('utf-8').strip())

lora_32.on_write(RX_Roport)

while True:
    getGPS.getGPS(gpsModule)
    
    if lora_32.is_connected() and getGPS.FIX_STATUS:
        # Short burst of queued notifications.
        lora_32.send("Printing GPS data..."+'\n')
        lora_32.send("Latitude: "+getGPS.latitude+'\n')
        lora_32.send("Longitude: "+getGPS.longitude+'\n')
        lora_32.send("Satellites: " +getGPS.satellites+'\n')
        lora_32.send("Time: "+getGPS.GPStime+'\n')
        lora_32.send("----------------------"+'\n')
        
    if lora_32.is_connected() and getGPS.TIMEOUT:
        lora_32.send("No GPS data is found."+'\n')
        lora_32.send("----------------------"+'\n')
        getGPS.TIMEOUT = False